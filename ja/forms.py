from django import forms
from django.contrib.auth.models import User
from .models import SalesForceModel

class SalesForm(forms.ModelForm):
	class Meta:
		model = SalesForceModel
		fields = ['username','password','security_token',]