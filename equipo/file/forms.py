from django import forms

class docform(forms.Form):
	docfile=forms.FileField(
	     label='Select your documents file',
	     help_text='(42MB max)'
	)
