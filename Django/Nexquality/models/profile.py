
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.db.models import Q, Avg, Sum
from Nexquality.models.profile_type import ProfileType
from Nexquality.models.project import Project
from Nexquality.models.metric import Metric


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

    def get_metrics_average_and_sum(self):
        if Metric.objects.filter(commit__user=self.user).count() > 0:
            return Metric.objects.filter(commit__user=self.user).values('field').annotate(
                    sum=Sum("calculated"), 
                    average=Avg("calculated")
                )
