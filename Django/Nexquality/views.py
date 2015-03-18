from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import forms
from django.utils.translation import ugettext as _


def index(request):
    return render(request, "index.html")


@login_required
def user_profile(request):
    return render(request, "accounts/profile.html")


def subscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = create_basic_user(form.cleaned_data)
            login(request, user)
            return user_profile
    else:
        form = UserCreationForm()

    return render(request, "registration/subscription.html", {
        'form': form
    })


def create_basic_user(cleaned_data):
    username = cleaned_data['username']
    password = cleaned_data['password']
    user = User.objects.create_user(username, password)
    user.first_name = cleaned_data['first_name']
    user.last_name = cleaned_data['last_name']
    user.email = cleaned_data['email']
    user.save()
    return user


class UserSubscriptionForm(forms.ModelForm):
    username = forms.CharField(min_length=5, max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=5, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True)

    def clean_password(self):
        if self.data['password'] != self.data['confirm_password']:
            raise forms.ValidationError(_('Password are not the same'))
        return self.data['password']

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'first_name', 'last_name', 'email']
