from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class IssueLevel(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
