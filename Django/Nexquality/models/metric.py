# -*- coding: utf-8 -*-
from django.db import models
from Nexquality.models.commit import Commit
from Nexquality.models.metric_field import MetricField


class Metric(models.Model):
    value = models.FloatField()
    field = models.ForeignKey(MetricField)
    commit = models.ForeignKey(Commit)
    calculated = models.FloatField(null=True)

    class Meta:
        ordering = ['field']

    def get_preceding(self):
        preceding_commit = self.commit.get_preceding()
        if preceding_commit is not None:
            return Metric.objects.get(commit=preceding_commit, field=self.field)
        else:
            return None

    def calculate_code_coverage(self):
        line_of_code_metric = Metric.objects.get(commit=self.commit, field__name="Line Of Code")
        line_of_code = line_of_code_metric.value
        preceding_line_of_code = line_of_code_metric.get_preceding().value
        covered_lines = (line_of_code * self.value/100) - (preceding_line_of_code * self.get_preceding().value/100)
        total_lines = line_of_code - preceding_line_of_code
        return (covered_lines / total_lines) * 100

    def calculate_complexity(self):
        return (self.value * 2) - self.get_preceding().value

    def calculate_duplicated_line_density(self):
        return (self.value * 2) - self.get_preceding().value

    def calculate_average_by_class(self):
        return (self.value * 2) - self.get_preceding().value

    def calculate_average_by_method(self):
        return (self.value * 2) - self.get_preceding().value

    def calculate_default(self):
        return self.value - self.get_preceding().value

    def calculation_factory(self):
        field_name = self.field.name
        if(field_name == "Code Coverage"):
            return self.calculate_code_coverage()
        elif(field_name == "Complexity"):
            return self.calculate_complexity()
        elif(field_name == "Duplicated Lines Density"):
            return self.calculate_duplicated_line_density()
        elif(field_name == "Average By Class"):
            return self.calculate_average_by_class()
        elif(field_name == "Average By Method"):
            return self.calculate_average_by_method()
        else:
            return self.calculate_default()

    def calculate(self):
        if self.get_preceding() is not None:
            return self.calculation_factory()
        else:
            return self.value
