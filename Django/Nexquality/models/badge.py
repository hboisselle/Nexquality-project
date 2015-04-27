# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from Nexquality.models.badge_category import BadgeCategory
from conditions import ConditionsField, conditions_from_module
from Nexquality.models.condition_types import badge_conditions


@python_2_unicode_compatible
class Badge(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=250)
    conditions = ConditionsField(
        definitions=conditions_from_module(badge_conditions))
    image = models.ImageField(upload_to='images/badges')
    score = models.IntegerField(default=0)
    category = models.ForeignKey(BadgeCategory, default=1)
    given_once = models.BooleanField(default=False)

    def __str__(self):
        return self.name
