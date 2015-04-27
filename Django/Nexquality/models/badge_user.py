# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from Nexquality.models.badge import Badge
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError


@python_2_unicode_compatible
class BadgeUser(models.Model):
    badge = models.ForeignKey(Badge)
    user = models.ForeignKey(User)
    attribution_date = models.DateTimeField(default=timezone.now())
    removal_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-attribution_date']

    def clean(self):
        if BadgeUser.objects.filter(badge=self.badge, user=self.user,
                                    badge__given_once=True,
                                    removal_date=None).exists():
            raise ValidationError("Badge can only be given once.")

    def __str__(self):
        return u"{0} - {1} - {2}".format(self.attribution_date, self.user.get_full_name(), self.badge.name)
