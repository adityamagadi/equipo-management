from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context
from equipo.evals.models import *
from equipo.evals.forms import *

def submitmarks(request):
	if request.method=='POST':
		form=evalform(request.POST)
		if form.is_valid():
			newmarks=marks(name=form.cleaned_data['name'],marks=form.cleaned_data['marks'])
			newmarks.save()
			return HttpResponseRedirect('success.html')
		else:
			form=evalform()
			context={'form':form}
			return render_to_response(
               		'/home/aditya/Desktop/finally/equipo/evals/templates/entermark.html',context,                		                        context_instance=RequestContext(request))
			
	else:
		form=evalform()
		return render_to_response(
               '/home/aditya/Desktop/finally/equipo/evals/templates/entermark.html',{'form':form},                		                 context_instance=RequestContext(request))
		
def success(request):
	log="login.png"
        l={'picture':log}
        return render_to_response('/home/aditya/Desktop/finally/equipo/evals/templates/success.html',l,RequestContext(request))
	

def viewmarks(request):
	
	m=marks.objects.all()
	return render_to_response(
        '/home/aditya/Desktop/finally/equipo/evals/templates/marklist.html',
        {'m': m},
        context_instance=RequestContext(request)
        )			


def guide_submitmarks(request):
	if request.method=='POST':
		form=guide_eval_form(request.POST)
		if form.is_valid():
			guide_newmarks=guide_marks(name1=form.cleaned_data['name1'],name2=form.cleaned_data				      				['name2'],name3=form.cleaned_data['name3'],name4=form.cleaned_data['name4'],usn1=form.cleaned_data['usn1'],
			usn2=form.cleaned_data['usn2'],usn3=form.cleaned_data['usn3'],usn4=form.cleaned_data['usn4'],
			marks1=form.cleaned_data['marks1'],projectname=form.cleaned_data['projectname'],
			marks2=form.cleaned_data['marks2'],marks3=form.cleaned_data['marks3'],marks4=form.cleaned_data['marks4'])
			guide_newmarks.save()
			return HttpResponseRedirect('success.html')
		else:
			form=guide_eval_form()
			context={'form':form}
			return render_to_response(
               		'/home/aditya/Desktop/finally/equipo/evals/templates/guidemarks.html',context,                		                        context_instance=RequestContext(request))
			
	else:
		form=guide_eval_form()
		context={'form':form}
		return render_to_response(
               '/home/aditya/Desktop/finally/equipo/evals/templates/guidemarks.html',context,                		                 context_instance=RequestContext(request))

def guide_viewmarks(request):
	
	g=guide_marks.objects.all()
	return render_to_response(
        '/home/aditya/Desktop/finally/equipo/evals/templates/guide_marklist.html',
        {'g': g},
        context_instance=RequestContext(request)
        )			
