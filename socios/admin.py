from django.contrib import admin
from .models import Socio

# Register your models here.

@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','edad','telefono','direccion','meses_pagos')
    ordering = ('apellido',)
    search_fields = ('nombre','apellido')


