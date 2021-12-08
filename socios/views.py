from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.template import Template, Context
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from socios.models import Mensaje

# Create your views here.
def home(request):
    plantilla_home = open('D:/proyecto final fullstack backend/healtyandfit/socios/templates/index.html')
    template = Template(plantilla_home.read())
    plantilla_home.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

@csrf_exempt
def registrar_mensaje(request):
    nombre = request.POST['name']
    email = request.POST['email']
    mensaje = request.POST['message']

    reg_mensaje = Mensaje.objects.create(nombre=nombre,email=email,mensaje=mensaje)
    return redirect('/')
    