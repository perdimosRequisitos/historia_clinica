from django.contrib.auth import authenticate
from historia.models import Paciente, HistoriaClinica
from faker import Faker


user = authenticate(username="Samuel", password="micontraseña123")

fake = Faker(locale="es_CO")

paciente = Paciente.objects.create(
    identificacion=fake.unique.random_number(digits=10),
    nombre_completo=fake.name(),
    fecha_nacimiento=fake.date_of_birth(),
    genero=fake.random_element(elements=("M", "F")),
    direccion=fake.address(),
    telefono=fake.phone_number(),
    etnia=fake.random_element(
        elements=("ninguna", "indigena", "afrocolombiano", "raizal", "rom")
    ),
    medico=user,
)

historia = HistoriaClinica.objects.create(
    paciente=paciente,
    grupo_antecedente=fake.random_element(elements=("personal", "familiar")),
    tipo_antecedente=fake.random_element(
        elements=("quirurgico", "alergico", "traumatico", "toxicologico")
    ),
    fecha=fake.date_this_decade(),
    descripcion=fake.text(),
)