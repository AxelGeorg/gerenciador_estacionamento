from django.urls import path

from . import views

app_name = "mainVagas"

urlpatterns = [
    path("", views.VagaList.as_view(), name="list"),
    path("create/", views.VagaCreate.as_view(), name="create"),
    path("update/<int:pk>/", views.VagaUpdate.as_view(), name="update"),
    path("detail/<int:pk>/", views.VagaDetail.as_view(), name="detail"),
    path("delete/<int:pk>/", views.VagaDelete.as_view(), name="delete"),
]
