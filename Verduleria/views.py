from django.shortcuts import render
from .models import Factura


def home(request):
    facts = Factura.objects.all()
    print(facts)
    return render(request, 'Verduleria/home.html', {"title": "jeje", "facturas": facts})


def detalle(request, pk):
    f = Factura.objects.get(pk=pk)
    pcs = f.productocantidad_set.all()

    return render(request, 'Verduleria/detalle.html', {'factura': f, 'productos': pcs})
