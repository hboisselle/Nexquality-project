from Nexquality.views import data_importation
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^xml/$', data_importation.UserXMLImporterCreateView.as_view(), name='xml'),
)
