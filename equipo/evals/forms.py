from django import forms
from django.forms import ModelForm
class evalform(forms.Form):
	name=forms.CharField(max_length=60)
	marks=forms.IntegerField()
	

class guide_eval_form(forms.Form):
	name1=forms.CharField(label=(u'name1'))
	name2=forms.CharField(max_length=60)
	name3=forms.CharField(max_length=60)
	name4=forms.CharField(max_length=60)
	usn1=forms.CharField(max_length=10) 
	usn2=forms.CharField(max_length=10)
	usn3=forms.CharField(max_length=10)
	usn4=forms.CharField(max_length=10)       
	projectname=forms.CharField(max_length=60)	
	marks1=forms.IntegerField()
	marks2=forms.IntegerField()
	marks3=forms.IntegerField()
	marks4=forms.IntegerField()

