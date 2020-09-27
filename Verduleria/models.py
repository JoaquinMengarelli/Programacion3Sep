from django.db import models

# Create your models here.

class dia(models.Model):
    fechadelacompra = models.DateTimeField()


class Productos(models.Model):
    tipodeproducto = models.CharField(max_length=15)
    producto = models.CharField(max_length=15)
    cantidadXkilo = models.CharField(max_length=15)
    precioXkilo = models.CharField(max_length=15)

class Cliente(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    dni = models.CharField(max_length=15)
    domicilio = models.CharField(max_length=15)

class Factura(models.Model):
    dia = models.CharField(max_length=15)
    Productos = models.CharField(max_length=15)
    Cliente = models.CharField(max_length=15)
    
