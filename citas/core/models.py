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
        default='NO_ESPECIFICA',
        max_length=50
    )

    personaFoto = models.ImageField(
        db_column='foto',
        upload_to='personas/',
        null=True
    )

    class Meta:
        db_table = 'personas'
        # ordering= ['-email','apellido']
        # unique_together = [['nombre','email'],['nombre','apellido','estado_civil']]

class CitaModel(models.Model):
    citaId = models.AutoField(
        primary_key=True,
        unique=True,
        db_column='id'
    )

    citaDescripcion = models.TextField(
        db_column='descripcion',
        null=False,
    )

    citaFecha = models.DateTimeField(
        db_column='fecha',
        null=False
    )

    citaLatitud = models.FloatField(
        db_column='latitud',
        null=False
    )

    citaLongitud = models.FloatField(
        db_column='longitud',
        null=False
    )

    opcionesEstado = [
        ('ACTIVA','ACTIVA'),
        ('CANCELADA','CANCELADA'),
        ('POSPUESTA','POSPUESTA')
    ]

    citaEstado = models.CharField(
        choices=opcionesEstado,
        db_column='estado',
        null=False,
        max_length=50
    )

    createAt = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at'
    )
    updateAt = models.DateTimeField(
        auto_now=True,
        db_column='update_at'
    )

    citador = models.ForeignKey(
        to=PersonaModel,
        db_column='citador_id',
        on_delete=models.PROTECT,
        related_name='personaCitas'
    )

    citado = models.ForeignKey(
        to=PersonaModel,
        db_column='citado_id',
        on_delete=models.PROTECT,
        related_name='personaCitadas'
    )

    class Meta:
        db_table = 'citas'
        unique_together = [['citaFecha','citador'],['citaFecha','citado']]
        ordering= ['-citaFecha']

# Create your models here.
