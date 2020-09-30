from django.contrib import admin
from .models import Factura
from .models import Cliente
from .models import Producto
from .models import ProductoCantidad
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_filter = ('tipodeproducto',)


#admin.site.register(ProductoCantidad)

class ProductoCantidadInline(admin.TabularInline):
    model = ProductoCantidad

class FacturaAdmin(admin.ModelAdmin):
    inlines = [ProductoCantidadInline]
#    list_display = ['cantidad', 'productos']

admin.site.register(Factura, FacturaAdmin)
#admin.site.register(Factura,FacturaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente)
#admin.site.register(ProductoCantidad)
