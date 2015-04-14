from xml.etree import ElementTree as ET
from django.contrib.auth.models import User
from Nexquality import models
from django.core.exceptions import ValidationError
import re


def split_on_caps(str):
    rs = [a for a in re.split(r'([A-Z][a-z]*)', str) if a]
    fs = ""
    rs[0] = rs[0].capitalize()
    for word in rs:
        fs += " "+word

    return fs.strip()


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


def parse_metric_category(parent_node):
    field_set = {}
    field_set['name'] = parent_node.tag.capitalize()
    metric_category, created = models.MetricCategory.objects.get_or_create(**field_set)
    if created: metric_category.save()
    return metric_category


def parse_metric_field(parent_node, category):
    field_set = {}
    name = split_on_caps(parent_node.tag)
    field_set['category'] = category
    field_set['name'] = name
    metric_field, created = models.MetricField.objects.get_or_create(**field_set)
    if created: metric_field.save()
    return metric_field



def parse_metrics(parent_node, commit):
    node = parent_node.find('metrics')
    for metric_category_node in node:
        category = parse_metric_category(metric_category_node)
        for metric_field_node in metric_category_node:
            field_set = {}
            field_set['field'] = parse_metric_field(metric_field_node, category)
            field_set['value'] = metric_field_node.text
            field_set['commit'] = commit
            metric = models.Metric(**field_set)
            metric.save()


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
        issue, created = models.Issue.objects.get_or_create(**kwargs)
        if created: issue.save()
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
        field_set['project'] = project
        commit = models.Commit(**field_set)
        commit.save()
        parse_metrics(node, commit)
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
    print('Importing project...')
    field_set = {}
    field_set['name'] = node.find('name').text
    field_set['created_by'] = request.user
    project, created = models.Project.objects.get_or_create(**field_set)
    if created: project.save()
    parse_project_users(node, project)
    parse_commits(node, project)
    print('Done!')
    print('Calculating metrics...')
    project.calculate_metrics()
    print('Done!')
