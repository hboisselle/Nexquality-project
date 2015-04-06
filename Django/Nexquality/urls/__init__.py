from django.conf.urls import patterns, url, include
from Nexquality.views import index, profile


urlpatterns = patterns('',
    url(r'^$', index.index, name='index'),
    url(r'^profile/$', profile.user_profile, name='profile'),
    url(r'^project/', include('Nexquality.urls.project', namespace='project')),
    url(r'^registration/', include('Nexquality.urls.registration', namespace="registration")),
    url(r'^data-importation/', include('Nexquality.urls.data_import', namespace="data_importation")),
)
