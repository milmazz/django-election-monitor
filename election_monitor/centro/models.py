#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from election_monitor.ubicacion.models import Estado, Circuito, \
                                              Municipio, Parroquia

class Centro(models.Model):
    """ Centros de votación """
    estado =  models.ForeignKey(Estado)
    circuito = ChainedForeignKey(Circuito, chained_field="estado", 
                                 chained_model_field="estado")
    municipio = ChainedForeignKey(Municipio, chained_field="circuito",
                                  chained_model_field="circuito")
    parroquia = ChainedForeignKey(Parroquia, chained_field="municipio",
                                  chained_model_field="municipio")
    nombre = models.CharField(max_length=128)
    direccion = models.TextField('Dirección')
    electores = models.PositiveIntegerField()
    mesas = models.PositiveIntegerField()
    latitud = models.CharField(max_length=16, blank=True)
    longitud = models.CharField(max_length=16, blank=True)
    # TODO: DELETE
    responsable = models.CharField(max_length=128, blank=True, null=True)
    telefono_responsable = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Centros de votación"

    def __unicode__(self):
        return self.nombre

class ResponsableCentro(models.Model):
     """ Responsable del Centro de Votacion """
     centro = models.OneToOneField(Centro)
     nombre = models.CharField(max_length=128, blank=True)
     telefono = models.CharField(max_length=32, blank=True)
     
     class Meta:
         verbose_name_plural = "Responsable del centro"
         
     def __unicode__(self):
        return self.nombre
