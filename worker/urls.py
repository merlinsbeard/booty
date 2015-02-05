from django.conf.urls import patterns, url

from worker import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^w/$', views.workers_index, name='workers'),
	url(r'^w/(?P<worker_id>\d+)/$', views.workers_solo, name='workers_solo'),
	

	url(r'^m/$', views.mall, name='malls'),
	url(r'^m/(?P<mall_id>\d+)/$', views.mall_solo, name='malls_solo'),

	url(r'^a/$', views.agency, name='agency'),
	url(r'^a/(?P<agency_id>\d+)/$', views.agency_solo, name='agency_solo'),


	)