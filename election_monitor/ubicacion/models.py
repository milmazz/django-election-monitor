#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Modelos de datos para Ubicaciones'''

from django.db import models
from smart_selects.db_fields import ChainedForeignKey

class Estado(models.Model):
    '''Informacion del estado'''
    estado = models.CharField(max_length=64, unique=True)

    class Meta:
        ordering = ('estado', )

    def __unicode__(self):
        ''':return: Representacion en cadena de la clase Estado'''
        return self.estado

    @models.permalink
    def get_absolute_url(self):
        return ('por_estado', (), {'estado': self.id})

class Circuito(models.Model):
    '''Informacion del circuito'''
    estado = models.ForeignKey(Estado)
    circuito = models.CharField(max_length=64)

    class Meta:
        unique_together = ('estado', 'circuito')
        ordering = ('estado', 'circuito')

    def __unicode__(self):
        ''':return: Representacion en cadena de la clase Circuito'''
        return self.circuito


class Municipio(models.Model):
    '''Informacion del Municipio'''
    estado = models.ForeignKey(Estado)
    circuito = ChainedForeignKey(Circuito, chained_field="estado",
                                 chained_model_field="estado")
    municipio = models.CharField(max_length=64)
    capital_estado = models.BooleanField()

    class Meta:
        unique_together = ("estado", "circuito", "municipio")
        ordering = ('estado', 'circuito', 'municipio')


    def __unicode__(self):
        ''':return: Representacion en cadena de la clase Municipio'''
        return self.municipio

    @models.permalink
    def get_absolute_url(self):
        return ('patrullas_por_municipio', (), {
            'estado': self.estado.id,
            'circuito': self.circuito.id,
            'municipio': self.id
        })


class Parroquia(models.Model):
    '''Informacion de la Parroquia'''
    estado = models.ForeignKey(Estado)
    circuito = ChainedForeignKey(Circuito, chained_field="estado",
                                 chained_model_field="estado")
    municipio = ChainedForeignKey(Municipio, chained_field="circuito",
                                  chained_model_field="circuito")
    parroquia = models.CharField(max_length=64)
    capital_municipio = models.BooleanField()

    class Meta:
        unique_together = ("estado", "circuito", "municipio", "parroquia")
        ordering = ('estado', 'circuito', 'municipio', 'parroquia')


    def __unicode__(self):
        ''':return: Representacion en cadena de la clase Parroquia'''
        return self.parroquia

    @models.permalink
    def get_absolute_url(self):
        return ('patrullas_por_parroquia', (), {
            'estado': self.estado.id,
            'circuito': self.circuito.id,
            'municipio': self.municipio.id,
            'parroquia': self.id
        })
