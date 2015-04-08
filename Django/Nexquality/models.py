#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.db.models import Q


@python_2_unicode_compatible
class Profile(models.Model):
    user = models.OneToOneField(User)
    rank = models.IntegerField(default=1)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def get_recent_projects(self):
        return Project.objects.filter(
            Q(created_by=self.user) |
            Q(users=self.user)
        ).distinct()[:5]


@python_2_unicode_compatible
class Project(models.Model):
    name = models.CharField(max_length=250, unique=True)
    start_date = models.DateField(default=timezone.now())
    is_done = models.BooleanField(default=False)
    users = models.ManyToManyField(User, through='ProjectUser')
    created_by = models.ForeignKey(User, related_name='project_starts')

    def get_latest_commit(self):
        if self.commit_set.count() > 0:
            return self.commit_set.order_by('-date')[0]
        else:
            return None

    def get_active_users(self):
        return self.projectuser_set.filter(out_date=None)

    def get_inactive_users(self):
        return self.projectuser_set.exclude(out_date=None)

    def save(self, *args, **kwargs):
        if self.is_done is True:
            for project_user in self.projectuser_set.all():
                project_user.inactivate()
                project_user.save()

        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class ProjectUserRole(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ProjectUser(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    role = models.ForeignKey(ProjectUserRole, default=1)
    in_date = models.DateField(default=timezone.now())
    out_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['out_date', 'in_date']

    def inactivate(self):
        self.out_date = timezone.now()


class Complexity(models.Model):
    complexity = models.FloatField()
    average_by_class = models.FloatField()
    average_by_method = models.FloatField()


class Coverage(models.Model):
    line_of_code = models.IntegerField()
    number_of_tests = models.IntegerField()
    number_of_failing_tests = models.IntegerField()
    number_of_ignored_tests = models.IntegerField()
    code_coverage = models.FloatField()


class Duplication(models.Model):
    duplicated_blocks = models.IntegerField()
    duplicated_lines = models.IntegerField()
    duplicated_lines_density = models.FloatField()


class Metrics(models.Model):
    complexity = models.OneToOneField(Complexity)
    coverage = models.OneToOneField(Coverage)
    duplication = models.OneToOneField(Duplication)


@python_2_unicode_compatible
class Violation(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class IssueLevel(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Issue(models.Model):
    description = models.CharField(max_length=255)
    level = models.ForeignKey(IssueLevel)
    violation = models.ForeignKey(Violation)

    def __str__(self):
        return self.description


@python_2_unicode_compatible
class Commit(models.Model):
    user = models.ForeignKey(User)
    revision = models.IntegerField()
    date = models.DateField()
    comment = models.CharField(max_length=500)
    project = models.ForeignKey(Project)
    metrics = models.OneToOneField(Metrics)
    issues = models.ManyToManyField(Issue)

    def __str__(self):
        return "Commit pushed on {1} by {2}".format(self.revision, self.date, self.user.get_full_name())
