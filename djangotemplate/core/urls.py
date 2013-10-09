from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	#url(r'^(.+)/$', 'core.views.method', name='method'),
	url(r'^home$', 'core.views.show_home', name='show_home'),
)
