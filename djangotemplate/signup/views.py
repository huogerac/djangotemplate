from django.views.generic.edit import FormView

from .forms import UserProfileRegistrationForm

class UserProfileRegistrationView(FormView):
	form_class = UserProfileRegistrationForm
	success_url = "/signup/accounts/registration/complete/"
	template_name = "signup/userprofile_registration.html"

	def post(self, request, *args, **kwargs):
		form = self.get_form(self.form_class)
		if form.is_valid():
			user = request.user
			user.first_name, user.last_name = request.POST['first_name'], request.POST['last_name']
			user.save()
			
		return self.form_valid(form)

	def form_valid(self, form):
		return super(UserProfileRegistrationView, self).form_valid(form)
