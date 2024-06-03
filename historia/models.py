from django.db import models
from datetime import date


# Create your models here.
class Paciente(models.Model):
    generos_validos = {
        "M": "Masculino",
        "F": "Femenino",
    }

    # Indigenas, Afrocolombianos, Raizales, Rom
    etnias_validas = {
        "ninguna": "Ninguna",
        "indigena": "Indígena",
        "afrocolombiano": "Afrocolombiano",
        "raizal": "Raizal",
        "rom": "Rom",
    }

    identificacion = models.CharField(max_length=20, primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1, choices=generos_validos, default="")
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    etnia = models.CharField(max_length=50, choices=etnias_validas, default="")

    def __str__(self) -> str:
        return f"{self.nombre_completo} ({self.identificacion})"

    def save(self, *args, **kwargs):
        self.nombre_completo = self.nombre_completo.upper()
        self.direccion = self.direccion.upper()
        return super().save(*args, **kwargs)

    def get_edad(self):
        return date.today().year - self.fecha_nacimiento.year


class Historia_Medica(models.Model):
    grupos_antecedentes = {
        "personal": "Personal",
        "familiar": "Familiar",
    }

    tipo_antecedentes = {
        "quirurgico": "Quirúrgico",
        "alergico": "Alergico",
        "traumatico": "Traumático",
        "toxicologico": "Toxicológico",
    }

    id_historia = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    grupo_antecedente = models.CharField(
        max_length=50, choices=grupos_antecedentes, default=""
    )
    tipo_antecedente = models.CharField(
        max_length=50, choices=tipo_antecedentes, default=""
    )
    fecha = models.DateField()
    descripcion = models.TextField()
