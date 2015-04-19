from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from Nexquality.models import Commit, MetricField, Badge


@login_required
def profile_detail(request, username):
    context = {}
    found_user = get_object_or_404(User, username=username)
    if found_user:
        average_metrics = []
        context['found_user'] = found_user
        context['commits'] = Commit.objects.filter(user=found_user)
        context['badge_count'] = Badge.objects.all().count()
        print(found_user.profile.rank)
        calculations = found_user.profile.get_metrics_calculations()
        if calculations:
            for calculation in calculations:
                metric = {}
                field_pk = calculation['field']
                metric['field'] = MetricField.objects.get(pk=field_pk)
                metric['average'] = calculation['average']
                metric['sum'] = calculation['sum']
                average_metrics.append(metric)
            context['metrics'] = average_metrics

        return render(request, "profile/detail.html", context)
