from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	#url(r'^(.+)/$', 'core.views.method', name='method'),
	url(r'^home$', 'core.views.show_home', name='show_home'),
	url(r'^examples$', 'core.views.show_examples', name='show_examples'),
	url(r'^themes$', 'core.views.show_themes', name='show_themes'),
	url(r'^themes_update$', 'core.views.update_themes', name='update_themes'),
	
)
