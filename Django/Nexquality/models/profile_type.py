#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class ProfileType(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
