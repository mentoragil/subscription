from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mentoragil.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('core.urls')),
    url(r'^subscription/', include('subscription.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
