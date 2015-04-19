
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.db.models import Q, Avg, Sum, Count
from Nexquality.models.profile_type import ProfileType
from Nexquality.models.project import Project
from Nexquality.models.metric import Metric
from Nexquality.models.badge import Badge


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

    def get_metrics_calculations(self):
        if Metric.objects.filter(commit__user=self.user).count() > 0:
            return Metric.objects.filter(commit__user=self.user).values(
                'field__name', 'field__category__name', 'field__unit',
                'field__unit', 'field__show_average', 'field__show_sum'
            ).annotate(
                sum=Sum("calculated"),
                average=Avg("calculated")
            )

    def get_recent_badges(self):
        return self.user.badgeuser_set.all().order_by('-attribution_date')[:5]

    def get_distinct_badge_count(self):
        return self.user.badgeuser_set.all().values('badge').distinct().count()

    def get_distinct_badge_count_by_category(self):
        return Badge.objects.annotate(total_badge_count=Count('id')).filter(
            badgeuser__user=self.user
        ).values(
            'category__name', 'total_badge_count'
        ).annotate(count=Count('id'))

    def get_commits(self):
        return self.user.commit_set.all()

    def get_badge_score(self):
        return self.user.badgeuser_set.all().aggregate(sum=Sum('badge__score'))['sum'] or 0
