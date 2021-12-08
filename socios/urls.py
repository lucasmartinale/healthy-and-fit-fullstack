from django.urls import path, include
from . import views
from socios.views import home, registrar_mensaje


urlpatterns = [
    path('', views.home, name='home'),
    path('enviar_formulario_contacto/', registrar_mensaje),
]