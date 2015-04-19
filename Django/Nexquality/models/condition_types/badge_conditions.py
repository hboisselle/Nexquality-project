from conditions import CompareCondition, Condition
from Nexquality.models import MetricField


class UnconditionalCondition(Condition):
    condstr = 'UNCONDITIONAL'

    def eval_bool(self, user, **kwargs):
        return False


def get_field_calculation_value(user, field_name, calculation_field):
    field_name = field_name.replace('_', ' ').strip()
    calculations = user.profile.get_metrics_calculations()
    field_id = MetricField.objects.get(name=field_name).id

    for calculation in calculations:
        if calculation['field'] == field_id:
            return calculation[calculation_field]


class AverageMetricCondition(CompareCondition):
    condstr = 'AVG_METRIC'

    def eval_operand(self, user, **kwargs):
        return get_field_calculation_value(user, self.key, 'average')


class SumMetricCondition(CompareCondition):
    condstr = 'SUM_METRIC'

    def eval_operand(self, user, **kwargs):
        return get_field_calculation_value(user, self.key, 'sum')
