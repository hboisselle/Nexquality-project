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
        metrics = []
        kwargs['found_user'] = found_user
        kwargs['commits'] = Commit.objects.filter(user=found_user)
        averages = found_user.profile.get_metrics_averages()
        for average in averages:
            metric = {}
            field_pk = average['field']
            metric['field'] = MetricField.objects.get(pk=field_pk)
            metric['average'] = average['average']
            metrics.append(metric)
        kwargs['metrics'] = metrics
        return render(request, "profile/detail.html", kwargs)
