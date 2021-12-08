from django.contrib import admin
from .models import Socio, Mensaje

# Register your models here.

@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','edad','telefono','direccion','meses_pagos')
    ordering = ('apellido',)
    search_fields = ('nombre','apellido')

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('nombre','email','mensaje')
    ordering = ('nombre',)
    search_fields = ('nombre',)

