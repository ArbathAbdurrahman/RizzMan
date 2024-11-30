from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import UserCreationForm
from django.core.exceptions import ValidationError

class LoginForm(AuthenticationForm):
	username = forms.CharField(
		max_length=256,
		widget = forms.TextInput()
	)

	password = forms.CharField(
		widget = forms.PasswordInput()
	)

	

