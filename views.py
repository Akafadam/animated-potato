from django.shortcuts import render
from .forms import Email, Password
from django.views.generic import TemplateView

class NameView(TemplateView):

	template_name = 'login/base.html'
	email_class = Email
	password_class = Password
	initial = {'key': 'value'}
	
	def get(self, request, *arg, **kwargs):
		email_input = self.email_class(initial=self.initial)
		password_input = self.password_class(initial=self.initial)
		return render(request, self.template_name, {'email': email_input, 'password': password_input,})
