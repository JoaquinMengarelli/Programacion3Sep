from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from Verduleria import views


urlpatterns = [
    path('', views.home, name='Verduleria-home'),
    path('admin', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),
    path('detalle/<pk>', views.detalle, name='Verduleria-detalle'),
]
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
