from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from .forms import PacienteForm


@login_required
def index(request: HttpRequest):
    return render(request, "historia/base.html")

def crear_paciente(request: HttpRequest):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('historia:index')
    else:
        form = PacienteForm()
    return render(request, 'historia/crear_paciente.html', {'form': form})
