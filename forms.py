from django import forms

class Email(forms.Form):
	email = forms.EmailField(label='', max_length='150')

class Password(forms.Form):
	Password =  forms.CharField(label='', min_length='6')