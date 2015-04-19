from conditions import CompareCondition, Condition


class UnconditionalCondition(Condition):
    condstr = 'UNCONDITIONAL'

    def eval_bool(self, user, **kwargs):
        return False


def get_field_calculation_value(user, field_name, calculation_field):
    field_name = field_name.replace('_', ' ').strip()
    calculations = user.profile.get_metrics_calculations()

    for calculation in calculations:
        if calculation['field'] == field_name:
            return calculation[calculation_field]


class AverageMetricCondition(CompareCondition):
    condstr = 'AVG_METRIC'

    def eval_operand(self, user, **kwargs):
        return get_field_calculation_value(user, self.key, 'average')


class SumMetricCondition(CompareCondition):
    condstr = 'SUM_METRIC'

    def eval_operand(self, user, **kwargs):
        return get_field_calculation_value(user, self.key, 'sum')


class SumSolvedIssuesCondition(CompareCondition):
    condstr = 'SUM_SOLVED_ISSUES'

    def eval_operand(self, user, **kwargs):
        solved_issues_count = 0
        for commit in user.profile.get_commits():
            solved_issues_count += commit.get_solved_issues().count()

        return solved_issues_count


class SumProjectCondition(CompareCondition):
    condstr = 'SUM_PROJECT'

    def eval_operand(self, user, **kwargs):
        return user.projectuser_set.all().count()