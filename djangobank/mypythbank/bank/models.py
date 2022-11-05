from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cuentas(models.Model):
    id = models.AutoField(primary_key=True)
    nrocuenta = models.IntegerField(max_length=20)
    nombre_prop = models.CharField(max_length=25)
    apell_prop = models.CharField(max_length=25)
    cedula_prop = models.IntegerField(max_length=20)
    saldo = models.DecimalField(max_digits=12, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

def __str__(self):
    return self.apell_prop

class Transfers(models.Model):
    id = models.AutoField(primary_key=True)
    emisora = models.ForeignKey(User, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    cta_receptora = models.IntegerField(max_length=20)
    ref = models.CharField(max_length=10)
    hora = models.DateTimeField(auto_now_add=True)
 