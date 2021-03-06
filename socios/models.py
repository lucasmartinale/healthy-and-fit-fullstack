from django.db import models

# Create your models here.
class Socio(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=40)
    meses_pagos = models.IntegerField()

class Mensaje(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    mensaje = models.CharField(max_length=500)