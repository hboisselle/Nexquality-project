from xml.etree import ElementTree as ET
from django.contrib.auth.models import User
from Nexquality.models import Project, Commit, ProjectUser, Metrics
from time import strptime


class XMLParser:
    """
    Class used to parse a XML file to Nexquality django models
    You must specify _file OR root of xml tree
    """
    def __init__(self, _file=None, root=None):
        self.tree = tree or ET.parse(_file)
        self.root = root or self.tree.getroot()


class UserXMLParser(XMLParser):
    def parse(self):
        for user_node in self.root.findall('user'):
            user = User()
            first_name, last_name = user_node.find('name').text.split(' ')
            user.first_name = first_name
            user.last_name = last_name
            user.set_password('123123')
            user.username = first_name[:4].lower() + last_name[:4].lower()
            user.email = user_node.find('email').text
            users.append(user.save())
        return users


class MetricsXMLParser(XMLParser):
    def parse(self):


class CommitXMLParser(XMLParser):
    def __init__(self, project, **kwargs):
        self.project = project

    def parse(self):
        for commit_node in self.root.findall('commit'):
            commit = Commit()
            commit.date = strptime(date, "%y-%m-%d")
            user_email = commit_node.find('user').text
            commit.user = User.objects.get(email=user_email)
            commit.comment = commit_node.find('comment').text
            metrics_root = commit.node.find('metrics')
            metrics = MetricsXMLParser(root=metrics_root)

    def add_user_to_project(self, user)



class ProjectXMLParser(XMLParser):
    def __init__(self, request, **kwargs):
        self.created_by = request.user

    def parse(self):
        for project_node in self.root.findall('project'):
            project = Project()
            project.name = project_node.find('name').text
            project.created_by = self.created_by
            project = project.save(commit=False)
            commit_root = project_node.find('commits')
            commits = CommitXMLParser(root=commit_root, project=project)
            project.commits = commits.parse()
            projects.append(project.save(commit=False))
        return projects
