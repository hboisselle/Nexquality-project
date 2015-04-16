from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from Nexquality.models.project import Project
from Nexquality.models.project_user_role import ProjectUserRole


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
