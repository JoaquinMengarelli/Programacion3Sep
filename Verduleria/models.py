from django.db import models

# Create your models here.

class Producto(models.Model):
    tipodeproducto = models.CharField(max_length=15)
    producto = models.CharField(max_length=15)
    cantidadXkilo = models.CharField(max_length=15)
    precioXkilo = models.CharField(max_length=15)


class Cliente(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    dni = models.CharField(max_length=15)
    domicilio = models.CharField(max_length=25)


class Factura(models.Model):
    Cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    fechadelacompra = models.DateTimeField()
