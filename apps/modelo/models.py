from django.db import models

# Create your models here.
class Cliente(models.Model):
    #equivale a enums en java
    listaGenero = (
        ('f', 'Femenino'),
        ('m', 'Masculino'),
    )
    listaEstadoCivil=(
        ('s', 'soltero'),
        ('c', 'casado'),
        ('d', 'divorciado'),
        ('v', 'viudo'),
    )
    #----------------------------------------componentes graficos
    cliente_id = models.AutoField(primary_key = True)
    cedula = models.CharField(max_length=10, unique = True,null = False)
    nombres = models.CharField(max_length=50, null = False)
    apellidos = models.CharField(max_length=50, null = False)
    direccion = models.TextField(max_length=50, default = 'sin direccion')
    telefono = models.CharField(max_length=10)
    genero = models.CharField(max_length=15, choices = listaGenero, default='Femenino', null= False)
    estadocivil = models.CharField(max_length= 20, choices= listaEstadoCivil, default='soltero' )
    #auto_now y auto_now_add atributos de configuracion de fecha
    fechaNacimiento= models.DateField(auto_now = False, auto_now_add = False, null= False )
    correo = models.EmailField(max_length=50, null = False)
    celular= models.CharField(max_length= 10)


class Cuenta(models.Model):
    listaTipo = (
        ('corriente', 'Corriente'),
        ('ahorros', 'Ahorros'),
    )
    cuenta_id = models.AutoField(primary_key= True)
    numero = models.CharField(max_length=28, unique= True, null=False)
    estado = models.BooleanField(default = True)
    fechaApertura = models.DateField(auto_now_add= True, null=False)
    tipoCuenta = models.CharField(max_length=30, choices=listaTipo, default="ahorros")
    saldo = models.DecimalField(max_digits = 10, decimal_places = 3, null = False)

    cliente = models.ForeignKey(
        'Cliente', 
        on_delete =models.CASCADE,
    )
    #equivalente a toString de java
    def _str_(self):
        string=str(self.saldo)+";"+str(self.cuenta_id)
        return string


class Transaccion(models.Model):
    listaTipoT = (
        ('retiro','Retiro'),
        ('deposito', 'Deposito'),
        ('transferencia', 'Transferencia'),
    )
    transaccion_id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add = True, null = False)
    tipo = models.CharField(max_length=30, choices=listaTipoT, null = False)
    valor = models.DecimalField(max_digits=10, decimal_places=3, null= False)
    descripcion = models.TextField(null = False)
    responsable = models.CharField(max_length=160, null = False)
    cuenta = models.ForeignKey(
        'Cuenta', 
        on_delete =models.CASCADE,
    )
