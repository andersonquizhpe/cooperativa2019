#copiar de archivo  urls.py
from django.urls import path
from . import views

#importar la direccion del metodo
urlpatterns = [
    path('', views.principal_pagina),
]
