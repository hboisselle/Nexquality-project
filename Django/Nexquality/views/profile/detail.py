from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from Nexquality.models import Badge


@login_required
def profile_detail(request, username):
    context = {}
    found_user = get_object_or_404(User, username=username)
    if found_user:
        context['badge_count'] = Badge.objects.all().count()
        context['profile'] = found_user.profile
        return render(request, "profile/detail.html", context)
