from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import Template, Context

# Create your views here.
def home(request):
    plantilla_home = open('D:/proyecto final fullstack backend/healtyandfit/socios/templates/index.html')
    template = Template(plantilla_home.read())
    plantilla_home.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)