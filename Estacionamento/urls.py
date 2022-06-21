from django.urls import path

from . import views

app_name = "Estacionamento"

urlpatterns = [
    path('', views.main, name='main'),
    path("gerenciaVagasList", views.gerenciaVagaList, name="gerenciaVagasList"),
    path('gerenciaVagasCreate/<int:pk>', views.gerenciaVagasCreate,
         name='gerenciaVagasCreate'),
    path("gerenciaVagasDetail/<int:pk>", views.gerenciaVagasDetail,
         name="gerenciaVagasDetail"),
]
