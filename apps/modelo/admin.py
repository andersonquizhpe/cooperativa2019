from django.contrib import admin
from .models import Cliente, Cuenta, Transaccion


#parentesis herencia para definir el superuser
class AdminCliente(admin.ModelAdmin):
    #listas-columnas
    list_display = ["cedula", "nombres", "apellidos", "genero"]
    #para que los campos sean editables
    list_editable = ["nombres", "apellidos"]
    #busqueda por filtros
    list_filter = ["genero","estadocivil"]

    search_fields = ["cedula", "apellidos"]
    #es la que permite vincular esta clase con el modelo

    class Meta:
        model = Cliente


class AdminCuenta(admin.ModelAdmin):
    list_display =["numero","tipoCuenta","estado","saldo", "cliente"]
    list_editable =["cliente"]
    list_filter = ["tipoCuenta", "estado", "cliente"]
    search_fields = ["tipoCuenta"]
    class Meta:
        model = Cuenta

class AdminTransaction(admin.ModelAdmin):
    list_display =["fecha","tipo","valor","responsable"]
    list_filter =["tipo"]
    search_fields=["fecha","tipo"]
    class Meta:
        model = Transaccion

admin.site.register(Cliente, AdminCliente)
admin.site.register(Cuenta, AdminCuenta)
admin.site.register(Transaccion, AdminTransaction)