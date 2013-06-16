
from django.conf.urls.defaults import patterns, include, url
from frontends.views import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from equipo.forum.views import *
from django.conf.urls.defaults import *
from equipo.forum.models import *
from django.conf.urls.static import static
from equipo.file.models import *

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'equipo.views.home', name='home'),
    # url(r'^equipo/', include('equipo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
		     #root url
                     (r'^$',login1),
                     #for hod login page
                     (r'^hodlogin.html$',hodlogin),
                     #for guide login page
                     (r'^guidelogin.html$',guidelogin),
                     #guide login page
                     (r'^teamlogin.html$',teamlogin),
                     (r'^hodnewdash.html$',hoddashboard),
                     
                     (r'^banner.html$',banner),
                     #options for hod
                     (r'^options2.html$',options2),
                     #upload documents
                     (r'^teamfile.html/$',"equipo.file.views.enterfile"),
                     (r'^teamfile.html/success.html$',"equipo.file.views.success"),
                     #hod evaluations:
                     
                     (r'^makeevaluation.html$',"equipo.evals.views.submitmarks"),
                     #viewing uploaded documents
                     (r'^uploads.html/$',"equipo.file.views.uploads"),
                     #uploading synopsis
                     (r'^createsynopsis.html/$',"equipo.synopsis.views.entersyns"),
                     (r'^createsynopsis.html/success.html$',"equipo.synopsis.views.success"),
                     #viewing uploaded synopsis
                     (r'^createdsynopsis.html$',"equipo.synopsis.views.upsyns"),
                     (r'^guidenewdash.html$',guidenewdash),
                     #options for guide
                     (r'^options1.html$',options1),
                     (r'something.html$',something),
                     (r'teamnewdash.html$',teamnewdash),
                     #options for team members
		     (r'options.html$',options),
                     #guide evaluations
                     (r'^guideevaluation.html$',"equipo.evals.views.guide_submitmarks"),
                     #hod evaluated marks
                     (r'viewgrades.html$',"equipo.evals.views.viewmarks"),
		     (r'logout',LogoutRequest),
                     
                     (r'^faqandreference.html$',fandr),
		     (r'^referencesection.html$',refsec),
		     #guide evaluated marks
                     (r'^viewguidegrades.html$',"equipo.evals.views.guide_viewmarks"),
                     #forum urls
                     (r"^forum/(\d+)/$", "equipo.forum.views.forum"),
                     (r"^thread/(\d+)/$", "equipo.forum.views.thread"),
                     (r"^post/(new_thread|reply)/(\d+)/$", "equipo.forum.views.post"),
                     (r"^reply/(\d+)/$", "equipo.forum.views.reply"),
                     (r"^profile/(\d+)/$", "equipo.forum.views.profile"),
                     (r"^new_thread/(\d+)/$", "equipo.forum.views.new_thread"),
                     (r"^generalforum.html$", "equipo.forum.views.main"),
		     (r"^success.html$", "equipo.evals.views.success"),
                     
                     
	
     )


#urls for serving static files
urlpatterns += patterns('',
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                       'document_root': settings.MEDIA_ROOT,}),
                       
                       )
