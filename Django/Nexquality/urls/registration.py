from django.conf.urls import patterns, url, include
from Nexquality.views import registration


urlpatterns = patterns('',
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^subscription/$', registration.subscription, name='subscription'),
)
