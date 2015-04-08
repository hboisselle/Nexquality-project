from data_importer.importers import XMLImporter
from Nexquality.models import *
from django.contrib.auth.models import User


class UserXMLImporter(XMLImporter):
    class Meta:
        model = User

    item_tag_name = 'user'
    fields = {'name', 'email'}
    field_map = {'username': 'email',
                 'first_name': 'name',
                 'email': 'email'}

    def save_item(self, item, data, instance, commit=True):
        instance.password = '123123'

        if commit:
            instance.save()
        return instance
