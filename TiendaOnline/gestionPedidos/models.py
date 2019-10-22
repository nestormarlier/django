from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField((""), max_length=30)
    direccion=models.CharField((""), max_length=50)
    email=models.EmailField((""), max_length=254)
    telefono=models.CharField((""), max_length=7)
    
class Articulos(models.Model):
    nombre=models.CharField((""), max_length=30)
    seccion=models.CharField((""), max_length=20)
    precio=models.IntegerField((""))
    
class Pedidos(models.Model):
    numero=models.IntegerField((""))
    fecha=models.DateField((""), auto_now=False, auto_now_add=False)
    entregado=models.BooleanField((""))