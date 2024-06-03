from django.contrib import admin
from .models import Paciente, HistoriaClinica

# Register your models here.
admin.site.register(Paciente)
admin.site.register(HistoriaClinica)
