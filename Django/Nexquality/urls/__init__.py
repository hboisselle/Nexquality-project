from django.conf.urls import patterns, url, include
from Nexquality.views import index
from django.conf import settings


urlpatterns = patterns('',
    url(r'^$', index.index, name='index'),
    url(r'^profile/', include('Nexquality.urls.profile', namespace='profile')),
    url(r'^project/', include('Nexquality.urls.project', namespace='project')),
    url(r'^registration/', include('Nexquality.urls.registration', namespace="registration")),
    url(r'^data-importation/', include('Nexquality.urls.data_import', namespace="data_importation")),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
