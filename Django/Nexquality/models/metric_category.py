# -*- coding: utf-8 -*-
from django.db import models


class MetricCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
