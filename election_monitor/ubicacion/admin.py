from django.contrib import admin
from election_monitor.ubicacion.models import Estado, Circuito, \
                                              Municipio,Parroquia

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('estado',)
    search_fields = ['estado',]
    ordering = ('estado', )

class CircuitoAdmin(admin.ModelAdmin):
    list_display = ('circuito', 'estado')
    list_filter = ['estado',]
    search_fields = ['estado',]

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('municipio', 'circuito', 'estado')
    list_filter = ['estado',]
    search_fields = ['estado', 'municipio']

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('parroquia', 'municipio', 'circuito', 'estado')
    list_filter = ['estado', 'municipio']
    search_fields = ['estado', 'municipio', 'parroquia']

admin.site.register(Estado, EstadoAdmin)
admin.site.register(Circuito, CircuitoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Parroquia, ParroquiaAdmin)
