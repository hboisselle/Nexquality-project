from Nexquality.importer import UserXMLParser
from django import forms
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def import_users_view(request):
    if request.method == 'POST':
        form = DataImportationForm(request.POST, request.FILES)
        if form.is_valid():
            _file = form.cleaned_data['_file']
            parser = UserXMLParser(_file=_file)
            parser.parse()
            return redirect(reverse('Nexquality:registration:login'))
    else:
        form = DataImportationForm()
    return render(request, "data_import/users.html", {'form': form})


class DataImportationForm(forms.Form):
    _file = forms.FileField(required=True)
