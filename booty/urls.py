from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'booty.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^info/', include('worker.urls')),
    url(r'^$', 'worker.views.index', name='home'),
    url(r'^search/', include('search.urls')),
)
