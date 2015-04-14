#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.db.models import Q, Avg, Max, Min, Sum
import re


@python_2_unicode_compatible
class ProfileType(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Profile(models.Model):
    user = models.OneToOneField(User)
    rank = models.IntegerField(default=1)
    profiletype = models.ForeignKey(ProfileType, default=1)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def get_recent_projects(self):
        return Project.objects.filter(
                Q(created_by=self.user) |
                Q(users=self.user)
            ).exclude(
                is_done=True
            ).distinct()[:5]

    def get_metrics_averages(self):
        if Metric.objects.filter(commit__user=self.user).count() > 0:
            return Metric.objects.filter(commit__user=self.user, field__show_average=True).values('field').annotate(average=Avg(("calculated"), output_field=models.FloatField()))
        else:
            return None

    def get_metrics_sums(self):
        if Metric.objects.filter(commit__user=self.user).count() > 0:
            return Metric.objects.filter(commit__user=self.user, field__show_sum=True).values('field').annotate(sum=Sum(("calculated"), output_field=models.FloatField()))
        else:
            return None


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

    def calculate_metrics(project):
        for commit in Commit.objects.filter(project=project):
            for metric in commit.metric_set.all():
                metric.calculated = metric.calculate()
                metric.save()

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


@python_2_unicode_compatible
class IssueLevel(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Violation(models.Model):
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
    date = models.DateTimeField()
    comment = models.CharField(max_length=500)
    project = models.ForeignKey(Project)
    issues = models.ManyToManyField(Issue)

    class Meta:
        ordering = ['-revision']

    def get_preceding(self):
        if not self.revision == 1:
            return Commit.objects.get(project=self.project, revision=self.revision - 1)
        else:
            return None

    def get_solved_issues(self):
        current_issues_ids = [issue.id for issue in self.issues.all()]
        return self.get_preceding().issues.exclude(id__in=current_issues_ids)

    def get_unsolved_issues(self):
        preceding_issues_ids = [issue.id for issue in self.get_preceding().issues.all()]
        return self.issues.filter(id__in=preceding_issues_ids)

    def get_new_issues(self):
        preceding_issues_ids = [issue.id for issue in self.get_preceding().issues.all()]
        return self.issues.exclude(id__in=preceding_issues_ids)

    def __str__(self):
        return "Commit pushed on {1} by {2}".format(self.revision, self.date, self.user.get_full_name())


class MetricCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MetricField(models.Model):
    category = models.ForeignKey(MetricCategory)
    name = models.CharField(max_length=50)
    unit =  models.CharField(max_length=50, null=True, blank=True)
    show_color = models.BooleanField(default=False)
    show_plus_sign = models.BooleanField(default=False)
    tolerance = models.FloatField(default=0)
    reverse_tolerance = models.BooleanField(default=False)
    show_average = models.BooleanField(default=True)
    show_sum = models.BooleanField(default=True)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return "{0} - {1}".format(self.category, self.name)


class Metric(models.Model):
    value = models.FloatField()
    field = models.ForeignKey(MetricField)
    commit = models.ForeignKey(Commit)
    calculated = models.FloatField(null=True)

    class Meta:
        ordering = ['field']

    def get_preceding(self):
        preceding_commit = self.commit.get_preceding()
        if preceding_commit is not None:
            return Metric.objects.get(commit=preceding_commit, field=self.field)
        else:
            return None

    def calculate_code_coverage(self):
        line_of_code_metric = Metric.objects.get(commit=self.commit, field__name="Line Of Code")
        line_of_code = line_of_code_metric.value
        preceding_line_of_code = line_of_code_metric.get_preceding().value

        covered_lines = (line_of_code * self.value/100) - (preceding_line_of_code * self.get_preceding().value/100)
        total_lines = line_of_code - preceding_line_of_code
        return (covered_lines / total_lines) * 100 

    def calculate_complexity(self):
        return (self.value * 2) - self.get_preceding().value

    def calculate_duplicated_line_density(self):
        return (self.value * 2) - self.get_preceding().value

    def calculate_average_by_class(self):
        return (self.value * 2) - self.get_preceding().value

    def calculate_average_by_method(self):
        return (self.value * 2) - self.get_preceding().value

    def calculate_default(self):
        return self.value - self.get_preceding().value

    def calculation_factory(self): 
        field_name = self.field.name
        if(field_name == "Code Coverage"):
            return self.calculate_code_coverage()
        elif(field_name == "Complexity"):
            return self.calculate_complexity()
        elif(field_name == "Duplicated Lines Density"):
            return self.calculate_duplicated_line_density()
        elif(field_name == "Average By Class"):
            return self.calculate_average_by_class()
        elif(field_name == "Average By Method"):
            return self.calculate_average_by_method()
        else:
            return self.calculate_default()

    def calculate(self):
        if self.get_preceding() is not None:
            return self.calculation_factory()
        else:
            return self.value
