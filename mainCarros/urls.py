from django.urls import path

from . import views

app_name = "mainCarros"

urlpatterns = [
    path("", views.CarroList.as_view(), name="list"),
    path("create/", views.CarroCreate.as_view(), name="create"),
    path("update/<int:pk>/", views.CarroUpdate.as_view(), name="update"),
    path("detail/<int:pk>/", views.CarroDetail.as_view(), name="detail"),
    path("delete/<int:pk>/", views.CarroDelete.as_view(), name="delete"),
]
