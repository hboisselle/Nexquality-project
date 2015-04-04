from xml.etree import ElementTree as ET
from django.contrib.auth.models import User
from Nexquality import models


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


def parse_coverage(parent_node):
    kwargs = {}
    node = parent_node.find('coverage')
    kwargs['line_of_code'] = node.find('lineOfCode').text
    kwargs['number_of_tests'] = node.find('numberOfTests').text
    kwargs['number_of_failing_tests'] = node.find('numberOfFailingTests').text
    kwargs['number_of_ignored_tests'] = node.find('numberOfIgnoredTests').text
    kwargs['code_coverage'] = node.find('codeCoverage').text
    coverage = models.Coverage(**kwargs)
    coverage.save()
    return coverage


def parse_complexity(parent_node):
    kwargs = {}
    node = parent_node.find('complexity')
    kwargs['complexity'] = node.find('complexity').text
    kwargs['average_by_class'] = node.find('averageByClass').text
    kwargs['average_by_method'] = node.find('averageByMethod').text
    complexity = models.Complexity(**kwargs)
    complexity.save()
    return complexity


def parse_duplication(parent_node):
    kwargs = {}
    node = parent_node.find('duplication')
    kwargs['duplicated_blocks'] = node.find('duplicatedBlocks').text
    kwargs['duplicated_lines'] = node.find('duplicatedLines').text
    kwargs['duplicated_lines_density'] = node.find('duplicatedLinesDensity').text
    duplication = models.Duplication(**kwargs)
    duplication.save()
    return duplication


def parse_metrics(parent_node):
    kwargs = {}
    node = parent_node.find('metrics')
    kwargs['complexity'] = parse_complexity(node)
    kwargs['duplication'] = parse_duplication(node)
    kwargs['coverage'] = parse_coverage(node)
    metrics = models.Metrics(**kwargs)
    metrics.duplication.save()
    metrics.complexity.save()
    metrics.coverage.save()
    metrics.save()
    return metrics


def parse_violation(parent_node):
    kwargs = {}
    kwargs['name'] = parent_node.find('violation').text
    violation, created = models.Violation.objects.get_or_create(**kwargs)
    if created: violation.save()
    return violation


def parse_issue_level(parent_node):
    kwargs = {}
    kwargs['name'] = parent_node.find('level').text
    issue_level, created = models.IssueLevel.objects.get_or_create(**kwargs)
    if created: issue_level.save()
    return issue_level


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
        kwargs = {}
        date = node.find('date').text
        kwargs['date'] = date[-4:]+"-"+date[3:5]+"-"+date[0:2]
        kwargs['revision'] = node.find('revision').text
        kwargs['user'] = User.objects.get(email=node.find('user').text)
        kwargs['comment'] = node.find('comment').text
        kwargs['metrics'] = parse_metrics(node)
        kwargs['project'] = project
        commit = models.Commit(**kwargs)
        commit.save()
        parse_issues(node, commit)


def parse_project_users(parent_node, project):
    for user_email_node in parent_node.findall('.//user'):
        kwargs = {}
        kwargs['user'] = User.objects.get(email=user_email_node.text)
        kwargs['project'] = project
        project_user, created = models.ProjectUser.objects.get_or_create(**kwargs)
        if created: project_user.save()


def parse_project(request, _file):
    tree = ET.parse(_file)
    node = tree.getroot()
    kwargs = {}
    kwargs['name'] = node.find('name').text
    kwargs['created_by'] = request.user
    project, created = models.Project.objects.get_or_create(**kwargs)
    if created: project.save()
    parse_project_users(node, project)
    parse_commits(node, project)
