from django.conf.urls import patterns, url

from Nexquality import views

urlpatterns = patterns('',
    url(r'^$', views.login_user, name='login_user')
)
