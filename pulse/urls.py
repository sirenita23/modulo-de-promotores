from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.middleware.csrf import CsrfViewMiddleware

urlpatterns = patterns('',
    # Examples:
    url(r'^$','django.contrib.auth.views.login',
        {'template_name':'inicio.html'} ,name = 'login'),

    url(r'^cerrar/$' , 'django.contrib.auth.views.logout_then_login',
         name='logout'),

    url(r'^evento/$', 'app.views.evento', name='evento'),
     #url(r'^Registrarse/$','app.views.Registrarse', name='Registrarse'),

    url(r'^add/$', 'app.views.add', name='add'),
    
    url(r'^Registrarse/$', 'Registrarse.as_view()', name='registrarse'),

    # url(r'^pulse/', include('pulse.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
