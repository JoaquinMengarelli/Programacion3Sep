from django.db import models

# Create your models here.

class Producto(models.Model):
    TIPO = (('1', 'Fruta'),
            ('2', 'Verdura'))
    tipodeproducto = models.CharField(max_length=1, choices=TIPO)
    nombre = models.CharField(max_length=15)
    precioXkilo = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    dni = models.IntegerField()
    domicilio = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre


class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#    productos = models.ManyToManyField(Producto)
    fechadelacompra = models.DateTimeField()
    #productocantidad = models.ManyToManyField(ProductoCantidad)
    preciototal = models.DecimalField(max_digits=5, decimal_places=2, editable=False, null=True)
#    ordering = ('fechadelacompra',)

    def save(self, *args, **kwargs):
        self.preciototal = sum([x.cantidad*x.productos.precioXkilo for x in self.productocantidad_set.all()])
        super().save(*args, **kwargs)

        #    def update_total(self):
 #       self.preciototal = sum([x.cantidad for x in self.productocantidad_set.all()])

    def __str__(self):
        fecha = self.fechadelacompra.strftime('%d/%m/%Y')
        return fecha

class ProductoCantidad(models.Model):
    cantidad = models.SmallIntegerField()
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)

