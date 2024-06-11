from django.db import models
from datetime import date


# Create your models here.
class Paciente(models.Model):
    generos_validos = {
        "": "Seleccione un género",
        "M": "Masculino",
        "F": "Femenino",
    }

    # Indigenas, Afrocolombianos, Raizales, Rom
    etnias_validas = {
        "": "Seleccione una etnia",
        "ninguna": "Ninguna",
        "indigena": "Indígena",
        "afrocolombiano": "Afrocolombiano",
        "raizal": "Raizal",
        "rom": "Rom",
    }

    id = models.AutoField(primary_key=True)
    identificacion = models.CharField(max_length=20, unique=True)
    nombre_completo = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(blank=True)
    genero = models.CharField(max_length=1, choices=generos_validos)
    direccion = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20)
    etnia = models.CharField(max_length=50, choices=etnias_validas)

    def __str__(self) -> str:
        return f"{self.nombre_completo} ({self.identificacion})"

    def save(self, *args, **kwargs):
        self.nombre_completo = self.nombre_completo.upper()
        self.direccion = self.direccion.upper()
        return super().save(*args, **kwargs)

    def get_edad(self):
        return date.today().year - self.fecha_nacimiento.year


class HistoriaClinica(models.Model):
    grupos_antecedentes = {
        "": "Seleccione un grupo",
        "personal": "Personal",
        "familiar": "Familiar",
    }

    tipo_antecedentes = {
        "": "Seleccione un tipo",
        "quirurgico": "Quirúrgico",
        "alergico": "Alergico",
        "traumatico": "Traumático",
        "toxicologico": "Toxicológico",
    }

    id_historia = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(
        Paciente, on_delete=models.CASCADE, to_field="identificacion", editable=True
    )
    grupo_antecedente = models.CharField(max_length=50, choices=grupos_antecedentes)
    tipo_antecedente = models.CharField(max_length=50, choices=tipo_antecedentes)
    fecha = models.DateField()
    descripcion = models.TextField()
    habilitado = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"historia {self.paciente.nombre_completo}"
