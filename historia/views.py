from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required, permission_required
from .forms import PacienteForm, HistoriaMedicaForm
from .models import Paciente, HistoriaClinica
from django.core.exceptions import PermissionDenied


@login_required
def index(request: HttpRequest):
    return render(request, "historia/base.html")


def crear_paciente(request: HttpRequest):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("historia:tabla_pacientes")
    else:
        form = PacienteForm()
    return render(request, "historia/crear_paciente.html", {"form": form})


def tabla_pacientes(request: HttpRequest):
    context = {}
    context["generos_validos"] = Paciente.generos_validos
    context["etnias_validas"] = Paciente.etnias_validas

    context["pacientes"] = Paciente.objects.all()

    filtro_sexo = request.GET.get("sexo")
    filtro_etnia = request.GET.get("etnia")
    if filtro_sexo:
        context["pacientes"] = context["pacientes"].filter(genero=filtro_sexo)
    if filtro_etnia:
        context["pacientes"] = context["pacientes"].filter(etnia=filtro_etnia)

    return render(request, "historia/tabla_pacientes.html", context)


def editar_paciente(request: HttpRequest, pk: int):
    paciente = Paciente.objects.get(pk=pk)
    if request.method == "POST":
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect("historia:tabla_pacientes")
    else:
        form = PacienteForm(instance=paciente)
    return render(request, "historia/editar_paciente.html", {"form": form})


def crear_historia(request: HttpRequest, pk: int):
    paciente = Paciente.objects.get(pk=pk)
    if request.method == "POST":
        form = HistoriaMedicaForm(request.POST)
        if form.is_valid():
            historia = form.save(commit=False)
            historia.paciente = paciente
            historia.save()
            return redirect("historia:tabla_pacientes")
    else:
        form = HistoriaMedicaForm()
    return render(
        request,
        "historia/crear_historia.html",
        {"form_historia": form, "paciente": paciente},
    )


def ver_historias(request: HttpRequest, paciente_id: str):
    historias = HistoriaClinica.objects.filter(paciente__identificacion=paciente_id)
    context = {
        "historias": historias,
        "paciente": Paciente.objects.get(identificacion=paciente_id),
    }
    return render(request, "historia/ver_historias.html", context)


def editar_historia(request: HttpRequest, pk: int):
    historia = HistoriaClinica.objects.get(pk=pk)
    if request.method == "POST":
        form = HistoriaMedicaForm(request.POST, instance=historia)
        if form.is_valid():
            form.save()
            return redirect(
                "historia:ver_historias",
                paciente_id=historia.paciente.identificacion,
                permanent=True,
            )
    else:
        form = HistoriaMedicaForm(instance=historia)
    return render(request, "historia/editar_historia.html", {"form": form})


@permission_required("historia.delete_paciente", raise_exception=True)
def eliminar_paciente(request: HttpRequest, pk: int):
    paciente = Paciente.objects.get(pk=pk)
    paciente.delete()
    return redirect("historia:tabla_pacientes")


def generar_tabla_pacientes(request: HttpRequest):
    context = {}
    context["pacientes"] = Paciente.objects.all()

    identificacion = request.GET.get("identificacion")

    if identificacion:
        context["pacientes"] = context["pacientes"].filter(
            identificacion__startswith=identificacion
        )

    return render(request, "historia/tabla.html", context)
