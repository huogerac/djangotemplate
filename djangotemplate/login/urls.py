from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = patterns('',
	url(r'^auth/$', auth_views.login, {'template_name': 'registration/login.html',
		                               'authentication_form': LoginForm},
       				                  name='url_login_auth'),
)
