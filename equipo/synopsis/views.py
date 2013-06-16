from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from equipo.synopsis.models import Synopsis
from equipo.synopsis.forms import synform

def entersyns(request):
	if request.method=='POST':
		form=synform(request.POST,request.FILES)
		if form.is_valid():
			newdoc = Synopsis(synfile = request.FILES['synfile'])
                        newdoc.save()
			return HttpResponseRedirect('success.html')
		else:
			form=synform()
			return render_to_response(
               '/home/aditya/Desktop/finally/equipo/synopsis/templates/upsyns.html',{'form':form},                		                         context_instance=RequestContext(request))
		
			
	else:
		form=synform()
		return render_to_response(
               '/home/aditya/Desktop/finally/equipo/synopsis/templates/upsyns.html',{'form':form},                		                         context_instance=RequestContext(request))
		
def success(request):
	log="login.png"
        l={'picture':log}
        return render_to_response('/home/aditya/Desktop/finally/equipo/synopsis/templates/success.html',l,RequestContext(request))

def upsyns(request):
	
	syns=Synopsis.objects.all()
	return render_to_response(
        '/home/aditya/Desktop/finally/equipo/synopsis/templates/syns.html',
        {'syns': syns},
        context_instance=RequestContext(request)
        )			
