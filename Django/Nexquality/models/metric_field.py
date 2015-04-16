from django.db import models
from Nexquality.models.metric_category import MetricCategory


class MetricField(models.Model):
    category = models.ForeignKey(MetricCategory)
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=50, null=True, blank=True)
    show_color = models.BooleanField(default=False)
    show_plus_sign = models.BooleanField(default=False)
    tolerance = models.FloatField(default=0)
    reverse_tolerance = models.BooleanField(default=False)
    show_average = models.BooleanField(default=True)
    show_sum = models.BooleanField(default=True)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return "{0} - {1}".format(self.category, self.name)
