from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User)
    rank = models.IntegerField(default=1)


class Project(models.Model):
    name = models.CharField(max_length=250, unique=True)
    start_date = models.DateField(default=timezone.now())
    is_done = models.BooleanField(default=False)
    users = models.ManyToManyField(User, through='ProjectUser')
    created_by = models.ForeignKey(User, related_name='project_starts')

    def __str__(self):
        return self.name


class ProjectUserRole(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def inactivate(self):
        self.out_date = timezone.now()


def inactivate_user_from_project(user, project):
    ProjectUser.objects.get(user=user, project=project).inactivate()


class ProjectUser(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    role = models.ForeignKey(ProjectUserRole, default=1)
    in_date = models.DateField(default=timezone.now())
    out_date = models.DateField(null=True, blank=True)
