from django.contrib import admin
from .models import Factura
from .models import Cliente
from .models import Producto
#from .models import ProductoCantidad
# Register your models here.

#admin.site.register(ProductoCantidad)

class FacturaInline(admin.TabularInline):
    model = Factura

class ClienteAdmin(admin.ModelAdmin):
    inlines = [FacturaInline]
    list_display= ('nombre','apellido')


admin.site.register(Factura)
admin.site.register(Producto)
admin.site.register(Cliente, ClienteAdmin)
