from xml.etree import ElementTree as ET
from django.contrib.auth.models import User
from Nexquality import models
from django.core.exceptions import ValidationError


def save_to_model(model, field_set, node, save=True, get_or_create=False):
    result_set = {}
    for model_field_name, source_field_name in field_set.items():
        value = node.find(source_field_name).text
        result_set[model_field_name] = value
    if(get_or_create):
        model, save = model.objects.get_or_create(**result_set)
    else:
        model = model(**result_set)
    if(save):
        model.save()
    return model


def parse_users(_file):
    tree = ET.parse(_file)
    root = tree.getroot()
    for node in root.findall('user'):
        user = User()
        first_name, last_name = node.find('name').text.split(' ')
        user.first_name = first_name
        user.last_name = last_name
        user.set_password('123123')
        user.username = first_name[:4].lower() + last_name[:4].lower()
        user.email = node.find('email').text
        user.save()
        parse_profile(user)


def parse_profile(user):
    profile = models.Profile(user=user)
    profile.save()


def parse_coverage(parent_node):
    field_set = {'line_of_code': 'lineOfCode',
        'number_of_tests': 'numberOfTests',
        'number_of_failing_tests': 'numberOfFailingTests',
        'number_of_ignored_tests': 'numberOfIgnoredTests',
        'code_coverage': 'codeCoverage'}
    node = parent_node.find('coverage')
    return save_to_model(models.Coverage, field_set, node)


def parse_complexity(parent_node):
    field_set = {'complexity': 'complexity',
        'average_by_class': 'averageByClass',
        'average_by_method': 'averageByMethod'}
    node = parent_node.find('complexity')
    return save_to_model(models.Complexity, field_set, node)


def parse_duplication(parent_node):
    field_set = {'duplicated_blocks': 'duplicatedBlocks',
        'duplicated_lines': 'duplicatedLines',
        'duplicated_lines_density': 'duplicatedLinesDensity'}
    node = parent_node.find('duplication')
    return save_to_model(models.Duplication, field_set, node)


def parse_metrics(parent_node):
    field_set = {}
    node = parent_node.find('metrics')
    field_set['complexity'] = parse_complexity(node)
    field_set['duplication'] = parse_duplication(node)
    field_set['coverage'] = parse_coverage(node)
    metrics = models.Metrics(**field_set)
    metrics.duplication.save()
    metrics.complexity.save()
    metrics.coverage.save()
    metrics.save()
    return metrics


def parse_violation(parent_node):
    field_set = {'name': 'violation'}
    return save_to_model(models.Violation, field_set, parent_node, get_or_create=True)


def parse_issue_level(parent_node):
    field_set = {'name': 'level'}
    return save_to_model(models.IssueLevel, field_set, parent_node, get_or_create=True)


def parse_issues(parent_node, commit):
    issues_node = parent_node.find('issues')
    for node in issues_node.findall('issue'):
        kwargs = {}
        kwargs['description'] = node.find('description').text
        kwargs['violation'] = parse_violation(node)
        kwargs['level'] = parse_issue_level(node)
        issue = models.Issue(**kwargs)
        issue.save()
        commit.issues.add(issue)
    commit.save()


def parse_commits(parent_node, project):
    commits_node = parent_node.find('commits')
    for node in commits_node.findall('commit'):
        field_set = {}
        date = node.find('date').text
        field_set['date'] = date[-4:]+"-"+date[3:5]+"-"+date[0:2]
        field_set['revision'] = node.find('revision').text
        field_set['user'] = User.objects.get(email=node.find('user').text)
        field_set['comment'] = node.find('comment').text
        field_set['metrics'] = parse_metrics(node)
        field_set['project'] = project
        commit = models.Commit(**field_set)
        commit.save()
        parse_issues(node, commit)


def parse_project_users(parent_node, project):
    for user_email_node in parent_node.findall('.//user'):
        field_set = {}
        try:
            field_set['user'] = User.objects.get(email=user_email_node.text)
        except models.User.DoesNotExist:
            raise ValidationError('Users in the project must exist to import the project.')
        field_set['project'] = project
        project_user, created = models.ProjectUser.objects.get_or_create(**field_set)
        if created: project_user.save()


def parse_project(request, _file):
    tree = ET.parse(_file)
    node = tree.getroot()
    field_set = {}
    field_set['name'] = node.find('name').text
    field_set['created_by'] = request.user
    project, created = models.Project.objects.get_or_create(**field_set)
    if created: project.save()
    parse_project_users(node, project)
    parse_commits(node, project)
