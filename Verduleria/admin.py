from django.contrib import admin
from .models import Factura
from .models import Cliente
from .models import Producto
from .models import ProductoCantidad
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_filter = ['tipodeproducto']
    list_display = ['nombre','precioXkilo']

class ClienteAdmin(admin.ModelAdmin):
     search_fields = ['nombre', 'apellido']
     list_display = ['nombre','apellido', 'domicilio', 'dni']




class ProductoCantidadInline(admin.TabularInline):
    model = ProductoCantidad

class FacturaAdmin(admin.ModelAdmin):
    inlines = [ProductoCantidadInline]
    search_fields = ['cliente']
    list_display = ['fechadelacompra','cliente', 'preciototal']
    ordering = ('fechadelacompra',)

    def post_save(self, instance):
        instance.update_total()

admin.site.register(Factura, FacturaAdmin)
#admin.site.register(Factura,FacturaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente, ClienteAdmin)
#admin.site.register(ProductoCantidad)
