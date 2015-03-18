from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User)
    rank = models.IntegerField(default=1)


class Project(models.Model):
    name = models.CharField(max_length=250)
    start_date = models.DateField(default=timezone.now())
    is_done = models.BooleanField(default=False)


class ProjectTeam(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
