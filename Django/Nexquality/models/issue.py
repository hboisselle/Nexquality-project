from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from Nexquality.models import Violation, IssueLevel


@python_2_unicode_compatible
class Issue(models.Model):
    description = models.CharField(max_length=255)
    level = models.ForeignKey(IssueLevel)
    violation = models.ForeignKey(Violation)

    def __str__(self):
        return self.description
