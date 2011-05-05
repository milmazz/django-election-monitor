from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# Serving static files in development
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    (r'^centros/', include('election_monitor.centro.urls')),
    (r'^exitpolls/', include('election_monitor.exitpolls.urls')),

    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name="logget_out"),
    
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),

    # Filtrado de Estados, Municipio, Parroquias
    (r'^chaining/', include('smart_selects.urls')),
)

#urlpatterns += staticfiles_urlpatterns()
from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views', 
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
