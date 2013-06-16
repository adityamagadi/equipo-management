from django import forms

class synform(forms.Form):
	synfile=forms.FileField(
	     label='Select your synopsis file',
	     help_text='(42MB max)'
	)
