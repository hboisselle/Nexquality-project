# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


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

    def get_available_users(self):
        return User.objects.filter

    def calculate_metrics(self):
        for commit in self.commit_set.all():
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
