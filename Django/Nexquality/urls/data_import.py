from Nexquality.views.data_import import xml_import
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^users/$', xml_import.import_users_view, name='users'),
)
