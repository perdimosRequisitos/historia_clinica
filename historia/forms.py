from django import forms
from .models import Paciente, HistoriaClinica
from datetime import date

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = "__all__"
        widgets = {
            "genero": forms.RadioSelect,
            "etnia": forms.RadioSelect,
            "fecha_nacimiento": forms.SelectDateWidget(years=range(date.today().year, 1900, -1)),
        }


class HistoriaMedicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = "__all__"
        widgets = {
            "grupo_antecedente": forms.RadioSelect,
            "tipo_antecedente": forms.RadioSelect,
            "fecha": forms.SelectDateWidget,
        }
