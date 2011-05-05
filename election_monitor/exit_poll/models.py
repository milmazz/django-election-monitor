#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
#from django.contrib.auth.models import User
#from django.http import HttpRequest
from smart_selects.db_fields import ChainedForeignKey

from election_monitor.ubicacion.models import Estado, Circuito, \
                                              Municipio, Parroquia
from election_monitor.centro.models import Centro
 
class ExitPoll(models.Model):
    estado =  models.ForeignKey(Estado)
    circuito = ChainedForeignKey(Circuito, chained_field="estado",
                                 chained_model_field="estado")
    municipio = ChainedForeignKey(Municipio, chained_field="circuito",
                                  chained_model_field="circuito")
    parroquia = ChainedForeignKey(Parroquia, chained_field="municipio",
                                  chained_model_field="municipio")
    centro_electoral = ChainedForeignKey(Centro, chained_field="parroquia",
                                         chained_model_field="parroquia")
    # Se asume que estos campos son PARCIALES
    # Una vez informada un exitpoll el entrevistador desecha esa hoja y reinicia
    # el conteo desde cero.
    votos_a_favor = models.PositiveIntegerField(help_text='Indique la diferencia \
                                                de votos a favor respecto a la \
                                                encuesta anterior')
    votos_en_contra = models.PositiveIntegerField(help_text='Indique la \
                                                  diferencia de votos en contra \
                                                  respecto a la encuesta \
                                                  anterior')
    no_contesto = models.PositiveIntegerField("no contestó", help_text='Indique \
                                              la diferencia de personas que no \
                                              respondieron respecto a la \
                                              encuesta anterior')
    votos_total = models.PositiveIntegerField(editable=False)

    #   TODO: Funcion para la extraccion de la IP del cliente
    #   def _get_ip_address():
    #        forwarded=request.META.get('HTTP_X_FORWARDED_FOR')
    #     if forwarded:
    #         return forwarded.split(',')[-1].strip()
    #     return request.META['REMOTE_ADDR']

    #
    # TODO: Ingresar direccion IP y usuario que hace registro de manera
    # automatica
    # usuario = models.ForeignKey(User)
    # direccion_ip = models.IPAddressField()
    enviado = models.DateTimeField(auto_now_add=True)

    def save(self):
        self.votos_total = self.votos_a_favor + self.votos_en_contra + self.no_contesto
        super(ExitPoll, self).save()

    class Meta:
        verbose_name_plural= "Exit Polls"
        ordering = ('-enviado',)
        get_latest_by = 'enviado'

    def __unicode__(self):
        return self.centro_electoral.nombre

    @models.permalink
    def get_absolute_url(self):
        return ('centro_electoral_results', (), {
            'estado': self.estado,
            'circuito': self.circuito,
            'municipio': self.municipio,
            'parroquia': self.parroquia,
            'centro_electoral': self.centro_electoral
        })
