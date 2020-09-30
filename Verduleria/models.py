from django.db import models

# Create your models here.

class Producto(models.Model):
    tipodeproducto = models.CharField(max_length=15)
    producto = models.CharField(max_length=15)
    cantidadXkilo = models.SmallIntegerField()
    precioXkilo = models.SmallIntegerField()


class Cliente(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    dni = models.IntegerField()
    domicilio = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre

class ProductoCantidad(models.Model):
    cantidad = models.SmallIntegerField()
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE)

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#    productos = models.ManyToManyField(Producto)
    fechadelacompra = models.DateTimeField()
    productocantidad = models.ManyToManyField(Producto)
    ordering = ('fechadelacompra',)
