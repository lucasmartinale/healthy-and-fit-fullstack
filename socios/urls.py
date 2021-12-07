from django.urls import path, include
from . import views
from socios.views import home

urlpatterns = [
    path('', views.home, name='home'),
]