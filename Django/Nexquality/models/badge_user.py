from django.db import models
from django.contrib.auth.models import User
from Nexquality.models.badge import Badge
from django.utils import timezone


class BadgeUser(models.Model):
    badge = models.ForeignKey(Badge)
    user = models.ForeignKey(User)
    attribution_date = models.DateTimeField(default=timezone.now())
    removal_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-attribution_date']

    def __str__(self):
        return "{0} - {1} - {2}".format(self.attribution_date, self.user.get_full_name(), self.badge.name)
