from django.contrib import admin

from election_monitor.exit_poll.models import ExitPoll

class ExitPollAdmin(admin.ModelAdmin):
    list_display = ('estado', 'circuito', 'municipio', 'parroquia',
                    'centro_electoral', 'votos_a_favor', 'votos_en_contra')
    list_filter = ['estado', 'municipio']
    search_fields = ['centro_electoral',]

admin.site.register(ExitPoll, ExitPollAdmin)
