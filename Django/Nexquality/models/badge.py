from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User


@python_2_unicode_compatible
class Badge(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    created_by = models.ForeignKey(User)
    conditions_code = models.CharField(max_length=4000, null=True, blank=True)
    image = models.ImageField(upload_to='images/badges')

    def __str__(self):
        return self.name
