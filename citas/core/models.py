from distutils.command.upload import upload
from pyexpat import model
from django.db import models

class PersonaModel(models.Model):
    personaId = models.AutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_column='id'
    )

    personaNombre = models.CharField(
        max_length=50,
        unique=False,
        null=False,
        db_column='nombre'
    )

    personaApellido = models.CharField(
        max_length=50,
        unique=False,
        null=False,
        db_column='apellido'
    )

    personaEmail = models.EmailField(
        max_length=50,
        db_column='email',
        null=False,
        unique=True
    )

    personaFechaNacimiento = models.DateField(
        db_column='fec_nac'
    )

    opcionesEstadoCivil = [
        ('SOLTERO','SOLTERO'),
        ('CASADO','CASADO'),
        ('VIUDO','VIUDO'),
        ('DIVORCIADO','DIVORCIADO'),
        ('COMPLICADO','COMPLICADO'),
        ('NO_ESPECIFICA','NO_ESPECIFICA')
    ]

    personaEstadoCivil = models.CharField(
        choices= opcionesEstadoCivil,
        db_column='estado_civil',
        default='NO_ESPECIFICA'
    )

    personaFoto = models.ImageField(
        db_column='foto',
        upload_to='personas/',
        null=True
    )

    class Meta:
        db_table = 'personas'
        # ordering= ['-email','apellido']

# Create your models here.
