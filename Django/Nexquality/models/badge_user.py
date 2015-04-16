from django.db import models
from django.contrib.auth.models import User
from Nexquality.models.badge import Badge
from django.utils import timezone


class BadgeUser(models.Model):
    badge = models.ForeignKey(Badge)
    user = models.ForeignKey(User)
    attributed_by = models.ForeignKey(User, related_name='badge_attributed_by')
    attribution_date = models.DateField(default=timezone.now())
    removal_date = models.DateField(null=True, blank=True)
