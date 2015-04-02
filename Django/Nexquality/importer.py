from xml.etree import ElementTree as ET
from django.contrib.auth.models import User
from Nexquality import models
from time import strptime


def parse_users(_file):
    tree = ET.parse(_file)
    root = tree.getroot()

    users = []
    for user_node in root.findall('user'):
        user = User()
        first_name, last_name = user_node.find('name').text.split(' ')
        user.first_name = first_name
        user.last_name = last_name
        user.set_password('123123')
        user.username = first_name[:4].lower() + last_name[:4].lower()
        user.email = user_node.find('email').text
        users.append(user.save())
    return users


def parse_coverage(root):
    node = root.find('coverage')
    coverage_metrics = models.CoverageMetrics()
    coverage_metrics.line_of_code = node.find('lineOfCode').text
    coverage_metrics.number_of_tests = node.find('numberOfTests').text
    coverage_metrics.number_of_failing_tests = node.find('numberOfFailingTests').text
    coverage_metrics.number_of_ignored_tests = node.find('numberOfIgnoredTests').text
    coverage_metrics.code_coverage = node.find('codeCoverage').text
    return coverage_metrics.save()


def parse_complexity(root):
    node = root.find('complexity')
    complexity_metrics = models.DuplicationMetrics()
    complexity_metrics.complexity = node.find('complexity').text
    complexity_metrics.average_by_class = node.find('averageByClass').text
    complexity_metrics.average_by_method = node.find('averageByMethod').text
    return complexity_metrics.save()


def parse_duplication(root):
    node = root.find('duplication')
    duplication_metrics = models.DuplicationMetrics()
    duplication_metrics.duplicated_blocks = node.find('duplicatedBlocks').text
    duplication_metrics.duplicated_lines = node.find('duplicatedLines').text
    duplication_metrics.duplicated_lines_density = node.find('duplicatedLinesDensity').text
    return duplication_metrics.save()


def parse_metrics(root):
    complexity = parse_complexity(root)
    duplication = parse_duplication(root)
    coverage = parse_coverage(root)

    metrics = models.Metrics()
    metrics.complexity = complexity
    metrics.duplication = duplication
    metrics.coverage = coverage
    return metrics.save()


def parse_commits(root):
    commits = []
    for node in root.findall('commit'):
        commit = models.Commit()

        date = node.find('date').text
        commit.date = strptime(date, "%d-%m-%Y")

        user_email = node.find('user').text
        commit.user = User.objects.get(email=user_email)
        commit.comment = node.find('comment').text

        metrics_root = node.find('metrics')
        commit.metrics = parse_metrics(metrics_root)

        commit.save()

        commits.append(commit)
    return commits


def parse_project_users(root, project):
    for user_email_node in root.findall('.//user'):
        user = User.objects.get(email=user_email_node.text)
        project_user, created = models.ProjectUser.objects.get_or_create(user=user, project=project)
        if created:
            project_user.save()


def parse_project(request, _file):
    tree = ET.parse(_file)
    node = tree.getroot()

    name = node.find('name').text
    created_by = request.user
    project, created = models.Project.objects.get_or_create(name=name, created_by=created_by)

    parse_project_users(root=node, project=project)

    # commit_root = node.find('commits')
    # project.commits = parse_commits(commit_root)

    return project.save()
