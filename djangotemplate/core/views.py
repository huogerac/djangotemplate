from django.shortcuts import redirect, render

def show_home(request):
	return render(request, 'core/home.html', {})
