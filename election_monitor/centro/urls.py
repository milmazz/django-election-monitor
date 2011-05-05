from django.conf.urls.defaults import *
from django.views.generic import ListView

from election_monitor.centro.models import Centro

urlpatterns = patterns('',
        # Index
        url(r'^$', ListView.as_view(
                model=Centro, 
                context_object_name='centro_list',
                template_name='centro/centro_list.html',
                allow_empty=True
            ),
            name="centros_index"),
        )
