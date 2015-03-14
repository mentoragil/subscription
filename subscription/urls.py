from django.conf.urls import patterns, url

from subscription import views

urlpatterns = patterns('',
    url(r'^subscribe/', views.subscribe, name='subscribe'),
    url(r'^success/', views.success),
    url(r'^failure/', views.failure),
    url(r'^subscribed/', views.already_subscribed),
)
