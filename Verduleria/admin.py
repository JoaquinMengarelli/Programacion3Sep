from django.contrib import admin
from .models import Factura
from .models import Cliente
from .models import Producto
from .models import ProductoCantidad
# Register your models here.

#admin.site.register(ProductoCantidad)

class ProductoCantidadInline(admin.TabularInline):
    model = ProductoCantidad

class FacturaAdmin(admin.ModelAdmin):
    inlines = [ProductoCantidadInline]
    list_display= ('fechadelacompra', 'cliente')

admin.site.register(Factura)
#admin.site.register(Factura,FacturaAdmin)
admin.site.register(Producto)
admin.site.register(Cliente)
