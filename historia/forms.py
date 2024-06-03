from django import forms
from .models import Paciente, Historia_Medica


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = "__all__"
        widgets = {
            "genero": forms.RadioSelect,
        }


class HistoriaMedicaForm(forms.ModelForm):
    class Meta:
        model = Historia_Medica
        fields = "__all__"
        widgets = {
            "grupo_antecedente": forms.RadioSelect,
            "tipo_antecedente": forms.RadioSelect,
        }
