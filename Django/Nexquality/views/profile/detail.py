from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from Nexquality.models import Commit, MetricField


@login_required
def profile_detail(request, username):
    context = {}
    found_user = get_object_or_404(User, username=username)
    if found_user:
        average_metrics = []
        context['found_user'] = found_user
        context['commits'] = Commit.objects.filter(user=found_user)
        print(found_user.profile.rank)
        metrics_average_sum = found_user.profile.get_metrics_average_and_sum()
        if metrics_average_sum:
            for metric_average_sum in metrics_average_sum:
                metric = {}
                field_pk = metric_average_sum['field']
                metric['field'] = MetricField.objects.get(pk=field_pk)
                metric['average'] = metric_average_sum['average']
                metric['sum'] = metric_average_sum['sum']
                average_metrics.append(metric)
            context['metrics'] = average_metrics

        return render(request, "profile/detail.html", context)
