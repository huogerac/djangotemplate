from django.shortcuts import redirect, render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from themes.views import get_themes
from .forms import ProfileForm

def show_home(request):
	return render(request, 'core/home.html', {})

def show_examples(request):
	return render(request, 'core/examples.html', {'myform': ProfileForm()})

def show_themes(request):
	themes = get_themes()
	return render(request, 'core/themes.html', {'themes':themes})

def update_themes(request):
	theme = request.GET.get('selected_theme', 'default')
	settings.THEME_NAME = theme
	return HttpResponseRedirect(reverse('show_home')) 

