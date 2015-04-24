# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from Nexquality.models.project import Project
from Nexquality.models.issue import Issue


@python_2_unicode_compatible
class Commit(models.Model):
    user = models.ForeignKey(User)
    revision = models.IntegerField()
    date = models.DateTimeField()
    comment = models.CharField(max_length=500)
    project = models.ForeignKey(Project)
    issues = models.ManyToManyField(Issue)
    code_review_score = models.FloatField(null=True)

    class Meta:
        ordering = ['-revision']

    def get_preceding(self):
        if not self.revision == 1:
            return Commit.objects.get(project=self.project, revision=self.revision - 1)
        else:
            return None

    def get_solved_issues(self):
        preceding_commit = self.get_preceding()
        if preceding_commit:
            current_issues_ids = [issue.id for issue in self.issues.all()]
            return self.get_preceding().issues.exclude(id__in=current_issues_ids)

    def get_unsolved_issues(self):
        preceding_commit = self.get_preceding()
        if preceding_commit:
            preceding_issues_ids = [issue.id for issue in preceding_commit.issues.all()]
            return self.issues.filter(id__in=preceding_issues_ids)

    def get_new_issues(self):
        preceding_commit = self.get_preceding()
        if preceding_commit:
            preceding_issues_ids = [issue.id for issue in self.get_preceding().issues.all()]
            return self.issues.exclude(id__in=preceding_issues_ids)
        else:
            return self.issues.all()

    def __str__(self):
        return "Commit pushed on {1} by {2}".format(self.revision, self.date, self.user.get_full_name())
