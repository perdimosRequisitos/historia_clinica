from django.urls import path

from . import views

app_name = "historia"
urlpatterns = [
    path("", views.index, name="index"),
    path("crear_paciente/", views.crear_paciente, name="crear_paciente"),
    path("tabla_pacientes/", views.tabla_pacientes, name="tabla_pacientes"),
    path("editar_paciente/<int:pk>/", views.editar_paciente, name="editar_paciente"),
    path("eliminar_paciente/<int:pk>/", views.eliminar_paciente, name="eliminar_paciente"),
    path("generar_tabla_pacientes/", views.generar_tabla_pacientes, name="generar_tabla_pacientes"),
    path("crear_historia/<int:pk>/", views.crear_historia, name="crear_historia"),
    path("editar_historia/<int:pk>/", views.editar_historia, name="editar_historia"),
]
