from django.conf.urls import patterns, url, include
from Nexquality.views import index


urlpatterns = patterns('',
    url(r'^$', index.index, name='index'),
    url(r'^profile/', include('Nexquality.urls.profile', namespace="profile")),
    url(r'^project/', include('Nexquality.urls.project', namespace='project')),
    url(r'^registration/', include('Nexquality.urls.registration', namespace="registration")),
    url(r'^data-importation/', include('Nexquality.urls.data_importation', namespace="data_importation")),
)
