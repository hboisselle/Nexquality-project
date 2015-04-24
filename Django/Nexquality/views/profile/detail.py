from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from Nexquality.models import Badge, MetricField, Profile
from Nexquality.reports.profile import ProfileChartData
from django.http import HttpResponse
import json


@login_required
def profile_detail(request, username):
    context = {}
    found_user = get_object_or_404(User, username=username)
    context['badge_count'] = Badge.objects.all().count()
    profile = found_user.profile
    context['profile'] = profile
    context['calculations'] = profile.get_metrics_calculations()
    context['users'] = User.objects.all()
    return render(request, "profile/detail.html", context)


def chart_json_data(request):
    data = {}
    params = request.GET

    name = params.get('name', 'metrics')
    field_name = params.get('field', 'Code Coverage')
    field_name = field_name.replace("_", " ")
    calculation = params.get('calculation', 'average')
    username = params.get('username', '')
    compared_profile_username = params.get('compared_profile', '')
    show_tolerance = bool(params.get('show_tolerance', False))
    show_average = bool(params.get('show_average', False))

    profile = Profile.objects.get(user__username=username)
    compared_profile = None
    if not compared_profile_username == '':
        compared_profile = Profile.objects.get(
            user__username=compared_profile_username)
    field = MetricField.objects.get(name=field_name)
    if name == 'metrics':
        data['chart_data'] = ProfileChartData.get_field_metrics(
            profile=profile, field=field, calculation=calculation,
            compared_profile=compared_profile, show_average=show_average,
            show_tolerance=show_tolerance)
    return HttpResponse(json.dumps(data), content_type='application/json')
