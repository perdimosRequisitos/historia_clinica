from django.urls import path

from . import views

app_name = "historia"
urlpatterns = [
    path("", views.index, name="index"),
    path("crear_paciente/", views.crear_paciente, name="crear_paciente"),
]
