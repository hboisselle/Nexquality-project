from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Profile(models.Model):
    user = models.OneToOneField(User)
    rank = models.IntegerField(default=1)

    def __str__(self):
        return self.user.name


@python_2_unicode_compatible
class Project(models.Model):
    name = models.CharField(max_length=250, unique=True)
    start_date = models.DateField(default=timezone.now())
    is_done = models.BooleanField(default=False)
    users = models.ManyToManyField(User, through='ProjectUser')
    created_by = models.ForeignKey(User, related_name='project_starts')

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

    def inactivate(self):
        self.out_date = timezone.now()


@python_2_unicode_compatible
class Commits(models.Model):
    user = models.ForeignKey(User)
    revision = models.IntegerField()
    date = models.DateField()
    comment = models.CharField(max_length=500)

    #TODO
    def __str__(self):
        return self.user + '-' + self.revision


class ComplexityMetrics(models.Model):
    complexity = models.FloatField()
    average_by_class = models.FloatField()
    average_by_method = models.FloatField()


class CoverageMetrics(models.Model):
    line_of_code = models.IntegerField()
    number_of_tests = models.IntegerField()
    number_of_failing_tests = models.IntegerField()
    number_of_ignored_tests = models.IntegerField()
    code_coverage = models.FloatField()


class DuplicationMetrics(models.Model):
    duplicated_blocks = models.IntegerField()
    duplicated_lines = models.IntegerField()
    duplicated_lines_density = models.IntegerField()


class Metrics(models.Model):
    complexity = models.ForeignKey(ComplexityMetrics)
    coverage = models.ForeignKey(CoverageMetrics)
    duplication = models.ForeignKey(DuplicationMetrics)
