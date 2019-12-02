from django import forms
from apps.modelo.models import Cliente, Cuenta, Transaccion

#creacion formularios
class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        #campos definidos de forma grafica
        fields = ["cedula", "nombres", "apellidos", "genero","fechaNacimiento","direccion","telefono","celular", "correo", "estadocivil"]

class FormularioModificarCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        #campos definidos de forma grafica
        fields = ["nombres", "apellidos", "genero","fechaNacimiento","direccion","telefono","celular", "correo", "estadocivil"]

class FormularioCuenta(forms.ModelForm):
    class Meta:
        model= Cuenta
        fields = ["numero", "saldo","tipoCuenta"]

class FormularioTransaccion(forms.ModelForm):
    class Meta:
        model= Transaccion
        fields = [ "valor","descripcion"]