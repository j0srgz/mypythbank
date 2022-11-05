from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Cuentas, Transfers
from decimal import Decimal
import string
import random

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    if request.method == 'POST':
        cuentaARegistrar = Cuentas.objects.get(nrocuenta = request.POST['nrocuenta'])
        if request.POST['password'] == request.POST['password2']:
            if cuentaARegistrar:
                if cuentaARegistrar.user_id:
                    failure = 'La cuenta ingresada ya posee un usuario en la plataforma'
                    return render(request, 'signup.html', {'failure': failure})
                else:
                    try:
                        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'], first_name=request.POST['nombre'], last_name=request.POST['apellido'])
                        login(request, user)
                        cuentaARegistrar.user_id = request.user.id
                        cuentaARegistrar.save()
                        return redirect('main')
                    except IntegrityError:
                        failure = 'El usuario ingresado ya existe, por favor, intente de nuevo'
                        return render(request, 'signup.html', {'failure': failure})
            else:
                failure = 'La cuenta ingresada no existe, por favor, verifique'
                return render(request, 'signup.html', {'failure': failure})
        else:
            failure = 'Las contraseñas ingresadas no coinciden, por favor verifique'
            return render(request, 'signup.html', {'failure': failure})

def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('main')
        else: 
            failure = 'Las credenciales son invalidas, por favor verifique'
            return render(request, 'login.html', {'failure': failure})

def main(request):
    if request.user.is_authenticated:
        cuenta = Cuentas.objects.get(user_id = request.user.id)
        return render(request, 'account.html', {'cuenta': cuenta})
    else:
        return redirect('/')


def reference(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def transfer(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            ctaactual = Cuentas.objects.get(user_id = request.user.id)
            return render(request, 'transfer.html', {'cuenta': ctaactual})
        if request.method == 'POST':
            ctaemisora = Cuentas.objects.get(nrocuenta = request.POST['ctaemisora'])
            ctareceptora = Cuentas.objects.get(nrocuenta = request.POST['ctareceptora'])
            monto = Decimal(request.POST['monto'])
            if ctareceptora:
                if ctaemisora.saldo > monto:
                    newSaldoCtaEmisora = ctaemisora.saldo - monto
                    ctaemisora.saldo = newSaldoCtaEmisora
                    ctaemisora.save()
                    newSaldoCtaReceptora = ctareceptora.saldo + monto
                    ctareceptora.saldo = newSaldoCtaReceptora
                    ctareceptora.save()
                    añadirRef = Transfers(
                        monto = request.POST['monto'],
                        cta_receptora = request.POST['ctareceptora'],
                        ref = reference(10),
                        emisora_id = request.user.id
                    )
                    añadirRef.save()
                    idRef = str(añadirRef.id)
                    return redirect('references/' + idRef)
    else:
        failure = 'Acceso denegado. Inicia sesión para realizar esta acción'
        return render(request, 'login.html', {'failure': failure})

def references(request, id):
    if request.user.is_authenticated:
        ref = Transfers.objects.get(pk = id)
        ctareceptora = Cuentas.objects.get(nrocuenta = ref.cta_receptora)
        ctaemisora = Cuentas.objects.get(user_id = ref.emisora_id)
        if ref.emisora_id == request.user.id or ctareceptora.user_id == request.user.id:
            return render(request, 'reference.html', {'ref': ref, 'ctareceptora': ctareceptora, 'ctaemisora': ctaemisora})
        else:
            return render(request, 'error403.html', status=403)
            
    else:
        failure = 'Acceso denegado. Inicia sesión para realizar esta acción'
        return render(request, 'login.html', {'failure': failure})

def history(request):
    if request.user.is_authenticated:
        ref = Transfers.objects.filter(emisora_id = request.user.id)
        return render(request, 'history.html', {'ref': ref})
    else:
        failure = 'Acceso denegado. Inicia sesión para realizar esta acción'
        return render(request, 'login.html', {'failure': failure})

def error404(request, exception):
    return render(request, 'error404.html', status=404)

def signout(request):
    logout(request)
    return redirect('/')



