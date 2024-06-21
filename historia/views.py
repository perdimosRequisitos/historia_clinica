from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required, permission_required
from .forms import PacienteForm, HistoriaMedicaForm
from .models import Paciente, HistoriaClinica
from django.core.exceptions import PermissionDenied


@login_required
def index(request: HttpRequest):
    return render(request, "historia/base.html")


@permission_required("historia.view_paciente", raise_exception=True)
def tabla_pacientes(request: HttpRequest):
    # context = {}
    # context["pacientes"] = Paciente.objects.all()
    # context["pacientes"] = Paciente.objects.filter(medico=request.user)
    # print(request.user)
    # context["pacientes"]

    return render(request, "historia/tabla_pacientes.html")


@permission_required("historia.add_paciente", raise_exception=True)
def crear_paciente(request: HttpRequest):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        print(form.errors)
        if form.is_valid():
            paciente: Paciente = form.save(commit=False)
            paciente.medico = request.user
            paciente.save()
            return redirect("historia:tabla_pacientes")
    else:
        form = PacienteForm()
    return render(request, "historia/crear_paciente.html", {"form": form})


@permission_required("historia.change_paciente", raise_exception=True)
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


@permission_required("historia.add_historiaclinica", raise_exception=True)
def crear_historia(request: HttpRequest, pk: int):
    paciente = Paciente.objects.get(pk=pk)
    if request.method == "POST":
        form = HistoriaMedicaForm(request.POST)
        if form.is_valid():
            historia = form.save(commit=False)
            historia.paciente = paciente
            historia.save()
            return redirect(
                "historia:ver_historias", paciente_id=paciente.identificacion
            )
    else:
        form = HistoriaMedicaForm()
    return render(
        request,
        "historia/crear_historia.html",
        {"form_historia": form, "paciente": paciente},
    )


@permission_required("historia.view_historiaclinica", raise_exception=True)
def ver_historias(request: HttpRequest, paciente_id: str):
    historias = HistoriaClinica.objects.filter(paciente__identificacion=paciente_id)
    context = {
        "historias": historias,
        "paciente": Paciente.objects.get(identificacion=paciente_id),
    }
    return render(request, "historia/ver_historias.html", context)


@permission_required("historia.change_historiaclinica", raise_exception=True)
def editar_historia(request: HttpRequest, pk: int):
    historia = HistoriaClinica.objects.get(pk=pk)
    paciente = historia.paciente
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
    return render(
        request, "historia/editar_historia.html", {"form": form, "paciente": paciente}
    )


@permission_required("historia.delete_paciente", raise_exception=True)
def eliminar_paciente(request: HttpRequest, pk: int):
    paciente = Paciente.objects.get(pk=pk)
    paciente.delete()
    return redirect("historia:tabla_pacientes")


def generar_tabla_pacientes(request: HttpRequest):
    context = {}
    # context["pacientes"] = Paciente.objects.all()
    context["pacientes"] = Paciente.objects.filter(medico=request.user)
    identificacion = request.GET.get("identificacion")

    if identificacion:
        context["pacientes"] = context["pacientes"].filter(
            identificacion__startswith=identificacion
        )

    return render(request, "historia/tabla.html", context)
