from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from Nexquality.models import Commit, MetricField


@login_required
def profile_detail(request, username):
    kwargs = {}
    found_user = get_object_or_404(User, username=username)
    if found_user:
        average_metrics = []
        kwargs['found_user'] = found_user
        kwargs['commits'] = Commit.objects.filter(user=found_user)
        print(found_user.profile.rank)
        averages = found_user.profile.get_metrics_averages()
        if averages:
            for average in averages:
                metric = {}
                field_pk = average['field']
                metric['field'] = MetricField.objects.get(pk=field_pk)
                metric['value'] = average['average']
                average_metrics.append(metric)
            kwargs['metrics_averages'] = average_metrics
        sums = found_user.profile.get_metrics_sums()
        sum_metrics = []
        if sums:
            for _sum in sums:
                metric = {}
                field_pk = _sum['field']
                metric['field'] = MetricField.objects.get(pk=field_pk)
                metric['value'] = _sum['sum']
                sum_metrics.append(metric)
            kwargs['metrics_sums'] = sum_metrics

        return render(request, "profile/detail.html", kwargs)
