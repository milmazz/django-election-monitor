from django.conf.urls.defaults import *

#from election_monitor.exit_poll.models import ExitPoll

urlpatterns = patterns('',
        url(r'^(?P<estado>\d+)/(?P<circuito>\d+)/(?P<municipio>\d+)/(?P<parroquia>\d+)/(?P<centro_electoral>\d+)/registrar/$',
            'election_monitor.exit_poll.views.registrar',
            name="exitpolls_registrar"
        ),
        url(r'^(?P<estado>\d+)/(?P<circuito>\d+)/(?P<municipio>\d+)/(?P<parroquia>\d+)/(?P<centro_electoral>\d+)/$',
            'election_monitor.exit_poll.views.centro_electoral_results',
            {'template_name': 'exitpolls/centro_list.html'},
            name="centro_electoral_results"
        ),

        url(r'^(?P<estado>\d+)/(?P<circuito>\d+)/(?P<municipio>\d+)/(?P<parroquia>\d+)/$',
            'election_monitor.exit_poll.views.parroquia_results',
            name="parroquia_results"
        ),
        url(r'^(?P<estado>\d+)/(?P<circuito>\d+)/(?P<municipio>\d+)/$',
            'election_monitor.exit_poll.views.municipio_results',
            name="municipio_results"
        ),
        url(r'^(?P<estado>\d+)/(?P<circuito>\d+)/$',
            'election_monitor.exit_poll.views.circuito_results',
            name="circuito_results"
        ),
        url(r'^(?P<estado>\d+)/$',
            'election_monitor.exit_poll.views.estado_results',
            name="estado_results"
        ),
        url(r'^$',
            'election_monitor.exit_poll.views.index',
            name="exitpolls_index"
        ),
)
