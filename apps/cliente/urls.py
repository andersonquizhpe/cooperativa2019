#copiar de archivo  urls.py
from django.urls import path
from . import views

#importar la direccion del metodo
urlpatterns = [
    path('', views.principal, name='cliente'),
    path('crear_cliente/', views.crear),
    path('modificar/', views.modificar),
    path('cuentas_cliente/', views.listarcuenta),
    path(r'^deposito/(?P<numero>d+)/$', views.depositar, name='deposito'),
    path(r'^retiro/(?P<numero>d+)/$', views.retirar, name='retiro'),
    path('crear_cuenta/(?P<cedula>d+)/$', views.crearCuenta, name='crear'),
    path('delete/(?P<cedula>d+)/$', views.eliminar, name='delete'),
    
]

#$ fin de url o definir .. 