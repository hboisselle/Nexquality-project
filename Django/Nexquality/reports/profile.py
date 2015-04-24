from Nexquality.models import Profile


class ProfileChartData(object):

    @classmethod
    def calculate_average_of_all_users(cls, field, calculation):
        average_value = 0
        i = 0
        for profile in Profile.objects.all():
            if profile.user.commit_set.exists():
                i = i+1
                calculations = profile.get_metrics_calculations(field=field)
                average_value = average_value + calculations[0][calculation]
        return (average_value / i)

    @classmethod
    def add_to_series(cls, series, name, data):
        series.append({
                'name': name,
                'data': data
            })
        return series

    @classmethod
    def get_field_metrics(
        cls,
        profile,
        field,
        calculation,
        compared_profile=None,
        show_average=False,
        show_tolerance=False
    ):
        profile_calculations = profile.get_metrics_calculations(field=field)

        data = {'fields': [], 'series': []}
        series = [{
            'name': profile.user.get_full_name(),
            'data': [profile_calculations[0][calculation]]
        }]

        if compared_profile is not None:
            compared_profile_calculations = compared_profile.get_metrics_calculations(field=field)
            series = cls.add_to_series(
                series,
                compared_profile.user.get_full_name(),
                [compared_profile_calculations[0][calculation]]
            )
        if show_average:
            average_of_all_users = cls.calculate_average_of_all_users(field, calculation)
            series = cls.add_to_series(
                series,
                'Average of all users',
                [average_of_all_users]
            )

        if calculation == "average" and show_tolerance:
            series = cls.add_to_series(
                series,
                'Tolerance',
                [profile_calculations[0]['field__tolerance']]
            )

        data['series'] = series
        data['fields'].append(field.name)
        return data
