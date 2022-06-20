from django.urls import path

from . import views

app_name = "Estacionamento"

urlpatterns = [
    path('', views.main, name='main'),
    path('gerenciaVagasCreate/<int:pk>', views.gerenciaVagasCreate,
         name='gerenciaVagasCreate'),
]
