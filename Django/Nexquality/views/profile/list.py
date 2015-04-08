from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def profile_list(request):
    users = User.objects.all()
    return render(request, "profile/list.html", {'users': users})
