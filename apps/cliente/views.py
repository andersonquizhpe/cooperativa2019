from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . form import FormularioCliente, FormularioCuenta, FormularioModificarCliente, FormularioTransaccion
from apps.modelo.models import Cliente, Cuenta, Transaccion

# Create your views here.
#ORM --> nos libra de proceso conceptual----->OR      SQLAlchemy
#@ ----> anotaciones 

@login_required
def principal(request):
    #actua con la base de datos
    lista= Cliente.objects.all().order_by('apellidos')
    context={
        'lista': lista,
        'title': 'COOPERATIVA QUINTO',
        'class': "form-control",
    }
    return render (request, 'cliente/principal_cliente.html', context)


#pedir autenticacion
@login_required
def crear(request):
    formulario = FormularioCliente(request.POST)
    #realcio con cuenta
    formularioCuenta = FormularioCuenta(request.POST)
    usuario = request.user #peticion procesada framework agrega el usuario

    if usuario.groups.filter(name = 'administrativo').exists():
        if request.method == 'POST':
            if formulario.is_valid() and formularioCuenta.is_valid():
                #obteniendo todos los datos del formulario Cliente
                datos = formulario.cleaned_data
                cliente = Cliente()
                cliente.cedula = datos.get('cedula')
                cliente.nombres = datos.get('nombres')
                cliente.apellidos = datos.get('apellidos')
                cliente.genero = datos.get('genero')
                cliente.fechaNacimiento = datos.get('fechaNacimiento')
                cliente.telefono = datos.get('telefono')
                cliente.celular = datos.get('celular')
                cliente.direccion = datos.get('direccion')
                cliente.correo = datos.get('correo')
                cliente.estadocivil = datos.get('estadocivil')
                cliente.save()
                datosCuenta = formularioCuenta.cleaned_data #----
                #creacion de objetos
                cuenta = Cuenta()
                cuenta.numero=datosCuenta.get('numero')
                cuenta.estado=True
                cuenta.saldo=datosCuenta.get('saldo')
                cuenta.tipoCuenta = datosCuenta.get('tipoCuenta')
                cuenta.cliente = cliente
                cuenta.save()
                return redirect(principal)
    else:
        print ('no tienes acceso')
        return render (request, 'cliente/acceso.html')
        #           |
        # REALIZAR  ----
        # 
        # instalar solo ---->(LUMEN) ....<laravel
        #
        # 
        # Administrativo----> clientes, cuentas. transacciones
        # cajer@ ------> transacciones --<> buscar cliente, cuenta y realizar transacciones
        # 
        # 
    #diccionarios
    context = {
        'f': formulario ,
        'fc': formularioCuenta,
        'title': 'COOPERATIVA QUINTO',
    }
    return render (request, 'cliente/crear_cliente.html', context)

@login_required
def modificar(request):
    dni = request.GET['cedula']
    cliente = Cliente.objects.get(cedula = dni)
    #enviar el cliente en formulario
  
    if request.method == 'POST':
        #modificar
        formulario = FormularioModificarCliente(request.POST)
        if formulario.is_valid():
            datos=formulario.cleaned_data
            cliente.nombres = datos.get('nombres')
            cliente.apellidos = datos.get('apellidos')
            cliente.genero = datos.get('genero')
            cliente.fechaNacimiento = datos.get('fechaNacimiento')
            cliente.telefono = datos.get('telefono')
            cliente.celular = datos.get('celular')
            cliente.direccion = datos.get('direccion')
            cliente.correo = datos.get('correo')
            cliente.estadocivil = datos.get('estadocivil')
            cliente.save() #save and update
            return redirect(principal)
            
    else:
        formulario = FormularioModificarCliente(instance=cliente)
    context ={
        'form': formulario,
        'title':'COOPERATIVA QUINTO',
    }
    return render (request , 'cliente/mod.html', context)

@login_required
def listarcuenta(request):
    dni = request.GET['cedula']
    cliente = Cliente.objects.get(cedula=dni)
    cuentas = Cuenta.objects.filter(cliente_id = cliente.cliente_id)
    context={
        'lista': cuentas,
        'cliente': cliente,
    }
    return render (request, 'cuenta/principal_cuenta.html', context)

@login_required
def depositar(request, numero):
    cuentas = Cuenta.objects.get(numero = numero)
    formulario = FormularioTransaccion(request.POST)
    cliente = Cliente.objects.get(cliente_id = cuentas.cliente_id)
    if request.method == 'POST':
        if formulario.is_valid():
            datos=formulario.cleaned_data
            cuentas.saldo = cuentas.saldo + datos.get('valor')
            cuentas.save()
            transaccion = Transaccion()
            transaccion.tipo = 'deposito'
            transaccion.valor = datos.get('valor')
            transaccion.descripcion = datos.get('descripcion')
            transaccion.responsable = 'Nina N.N'
            transaccion.cuenta = cuentas
            transaccion.save()
            #deposito = float (datos.get('valor'))
            #locals() ---> enviar atributos a la vista
            return render(request,'transaccion/estado.html')            
    context = {
        'cliente':cliente,
        'cuenta': cuentas,
        'formulario': formulario,
    }
    return render(request, 'transaccion/depositar.html', context)

@login_required
def retirar(request, numero):
    cuentas = Cuenta.objects.get(numero = numero)
    formulario = FormularioTransaccion(request.POST)
    cliente = Cliente.objects.get(cliente_id = cuentas.cliente_id)
    if request.method == 'POST':
        if formulario.is_valid():
            if (cuentas.saldo != 0 ):
                datos=formulario.cleaned_data
                cuentas.saldo = cuentas.saldo - datos.get('valor')
                cuentas.save()
                transaccion = Transaccion()
                transaccion.tipo = 'retiro'
                transaccion.valor = datos.get('valor')
                transaccion.descripcion = datos.get('descripcion')
                transaccion.responsable = 'Nina N.N'
                transaccion.cuenta = cuentas
                transaccion.save()
            #locals() ---> enviar atributos a la vista
            return render(request,'transaccion/estado.html')            
    context = {
        'cliente':cliente,
        'cuenta': cuentas,
        'formulario': formulario,
    }
    return render(request, 'transaccion/depositar.html', context)

@login_required
def crearCuenta(request, cedula):
    clientes = Cliente.objects.get(cedula=cedula)
    cliente = Cliente.objects.get(cliente_id=clientes.cliente_id)
    formularioCuenta = FormularioCuenta(request.POST)
    if request.method == 'POST':
        if  formularioCuenta.is_valid():
            #obteniendo todos los datos del formulario Cliente
            datosCuenta = formularioCuenta.cleaned_data #----
            #creacion de objetos
            cuenta = Cuenta()
            cuenta.numero=datosCuenta.get('numero')
            cuenta.estado=True
            cuenta.saldo=datosCuenta.get('saldo')
            cuenta.tipoCuenta = datosCuenta.get('tipoCuenta')
            cuenta.cliente = cliente
            cuenta.save()
            return redirect(principal)
    #diccionarios
    context = {
        'fc': formularioCuenta,
        'title': 'COOPERATIVA QUINTO',
    }
    return render (request, 'cuenta/nuevaCuenta.html', context)

@login_required
def eliminar(request, cedula):
    cliente = Cliente.objects.get(cedula=cedula)
    cliente.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('/cliente')
