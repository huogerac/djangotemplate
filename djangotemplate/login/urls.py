from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

from .forms import LoginForm

urlpatterns = patterns('',
	
	#login
	url(r'^auth/$', auth_views.login, {'template_name': 'login/login.html',
		                               'authentication_form': LoginForm}, name='url_login_auth'),

	#logout
    url(r'^logout/$', auth_views.logout,
       			{'template_name': 'login/logout.html'}, name='auth_logout'),

	#password reset
	url(r'^password/reset/$', auth_views.password_reset, 
				{'template_name': 'login/password_reset_form.html'}, name='url_login_password_reset'),
	
	url(r'^password/reset/done/$', auth_views.password_reset_done,
    			{'template_name': 'login/password_reset_done.html'}, name='auth_password_reset_done'),	

    url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, 
    			{'template_name': 'login/password_reset_confirm.html'}, name='auth_password_reset_confirm'),

    url(r'^password/reset/complete/$', auth_views.password_reset_complete,
    			{'template_name': 'login/password_reset_complete.html'}, name='auth_password_reset_complete'),
)
