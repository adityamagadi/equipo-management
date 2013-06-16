from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from frontends.models import newuser


class LoginForm(forms.Form):
        username        = forms.CharField(label=(u'User Name'))
        password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
	AuthID		= forms.IntegerField(label=(u'authid'))	
