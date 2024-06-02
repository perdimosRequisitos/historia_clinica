from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Paciente(models.Model):

    generos_validos = {
        'M': 'Masculino',
        'F': 'Femenino',
    }

    # Indigenas, Afrocolombianos, Raizales, Rom 
    etnias_validas = {
        'ninguna': 'Ninguna',
        'indigena': 'Indígena',
        'afrocolombiano': 'Afrocolombiano',
        'raizal': 'Raizal',
        'rom': 'Rom',
    }

    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)
    # identificacion = models.CharField(max_length=50, primary_key=True)
    etnia = models.CharField(max_length=50, choices=etnias_validas, default='')
    edad = models.PositiveIntegerField()
    genero = models.CharField(max_length=1, choices=generos_validos, default='')

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellidos}"
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.capitalize()
        self.apellidos = self.apellidos.capitalize()
        return super().save(*args, **kwargs)
