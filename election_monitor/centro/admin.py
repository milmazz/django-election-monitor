from django.contrib import admin
from election_monitor.centro.models import Centro, ResponsableCentro

class ResponsableCentroInline(admin.TabularInline):
    model = ResponsableCentro

class CentroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado', 'municipio', 'parroquia', 'circuito')
    list_filter = ['estado', 'municipio', 'parroquia']
    search_fields = ['nombre']
    inlines = [ResponsableCentroInline,]

admin.site.register(Centro, CentroAdmin)
