from data_importer.views import DataImporterForm
from Nexquality.importer import UserXMLImporter
from django.contrib.auth.models import User


class UserXMLImporterCreateView(DataImporterForm):
    importer = UserXMLImporter
    template_name = "data_importation/xml_importation.html"
    model = User
