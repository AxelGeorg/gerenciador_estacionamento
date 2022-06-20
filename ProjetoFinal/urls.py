
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Estacionamento.urls")),
    path('carros/', include("mainCarros.urls")),
    path('vagas/', include("mainVagas.urls")),
    path('clientes/', include("mainClientes.urls")),
]
