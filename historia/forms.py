from django import forms
from .models import Paciente, HistoriaClinica
# from datetime import date


class PacienteForm(forms.ModelForm):
        # https://docs.djangoproject.com/en/5.0/ref/forms/widgets/#styling-widget-instances
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                "class": "input input-bordered w-full max-w-xs"
            })

    class Meta:
        model = Paciente
        fields = "__all__"
        exclude = ["medico"]
        widgets = {
            # "genero": forms.RadioSelect,
            # "etnia": forms.RadioSelect,
            "fecha_nacimiento": forms.DateInput(
                attrs={"type": "date"}, format="%Y-%m-%d"
            ),
        }



        error_messages = {
            "nombre_completo": {"required": "Por favor, ingrese un nombre"},
            "genero": {"required": "Por favor, seleccione un género"},
            "etnia": {"required": "Por favor, seleccione una etnia"},
        }

    # todo: organizar
    template_name = "historia/custom_form.html"



class CrearHistoriaClinicaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["grupo_antecedente"].widget.attrs.update({"class": "daisyui-select"})
        self.fields["tipo_antecedente"].widget.attrs.update({"class": "daisyui-select"})
        self.fields["fecha"].widget.attrs.update({"class": "input input-bordered w-full max-w-xs"})
        self.fields["descripcion"].widget.attrs.update({"class": "daisyui-textarea"})
        self.fields["habilitado"].widget.attrs.update({"class": "daisyui-checkbox"})

    class Meta:
        model = HistoriaClinica
        fields = "__all__"
        exclude = ["paciente", "justificacion_modificacion"]
        widgets = {
            # "grupo_antecedente": forms.RadioSelect,
            # "tipo_antecedente": forms.RadioSelect,
            "fecha": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "descripcion": forms.Textarea(attrs={"rows": 5, "cols": 25}),
        }

    template_name = "historia/custom_form.html"


class EditarHistoriaClinicaForm(CrearHistoriaClinicaForm):
    class Meta:
        model = HistoriaClinica
        fields = "__all__"
        exclude = ["paciente"]
        widgets = {
            # "grupo_antecedente": forms.RadioSelect,
            # "tipo_antecedente": forms.RadioSelect,
            "fecha": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "descripcion": forms.Textarea(attrs={"rows": 5, "cols": 25}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["justificacion_modificacion"].widget.attrs.update(
            {
                "class": "daisyui-textarea",
                "rows": "5",
                "cols": "25",
             }
        )

    template_name = "historia/custom_form.html"