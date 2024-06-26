# Generated by Django 5.0.6 on 2024-06-10 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiaclinica',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='grupo_antecedente',
            field=models.CharField(choices=[('', 'Seleccione un grupo'), ('personal', 'Personal'), ('familiar', 'Familiar')], max_length=50),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='tipo_antecedente',
            field=models.CharField(choices=[('', 'Seleccione un tipo'), ('quirurgico', 'Quirúrgico'), ('alergico', 'Alergico'), ('traumatico', 'Traumático'), ('toxicologico', 'Toxicológico')], max_length=50),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='etnia',
            field=models.CharField(choices=[('', 'Seleccione una etnia'), ('ninguna', 'Ninguna'), ('indigena', 'Indígena'), ('afrocolombiano', 'Afrocolombiano'), ('raizal', 'Raizal'), ('rom', 'Rom')], max_length=50),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='genero',
            field=models.CharField(choices=[('', 'Seleccione un género'), ('M', 'Masculino'), ('F', 'Femenino')], max_length=1),
        ),
    ]
