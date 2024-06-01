from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = "__all__"
        widgets = {
                    'genero': forms.RadioSelect,
                    'edad': forms.NumberInput(attrs={'max': '150', 'min': '0'}),
                }
