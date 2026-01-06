from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator


class Paciente(models.Model):

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('I', 'Intersexual'),
        ('N', 'Prefiere no decir'),
    ]

    # Identificación
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150, blank=True)
    documento = models.CharField(max_length=50, unique=True)

    sexo = models.CharField(
        max_length=1,
        choices=SEXO_CHOICES,
        blank=True
    )

    fecha_nacimiento = models.DateField(
        null=True,
        blank=True
    )

    # Contacto
    telefono = models.CharField(max_length=30, blank=True)
    correo = models.EmailField(blank=True)

    # Familiar / responsable
    familiar_nombre = models.CharField(max_length=200, blank=True)
    familiar_parentesco = models.CharField(max_length=100, blank=True)
    familiar_telefono = models.CharField(max_length=30, blank=True)

    @property
    def edad(self):
        if not self.fecha_nacimiento:
            return None
        hoy = date.today()
        return hoy.year - self.fecha_nacimiento.year - (
            (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )

    edad.fget.short_description = "Edad"

    def __str__(self):
        return f"{self.nombres} {self.apellidos}".strip()


class NotaEnfermeria(models.Model):

    EVOLUCION_CHOICES = [
        ('1', 'Evolución 1'),
        ('2', 'Evolución 2'),
        ('3', 'Evolución 3'),
        ('4', 'Evolución 4'),
        ('5', 'Evolución 5'),
        ('6', 'Evolución 6'),
        ('X', 'Evolución extraordinaria'),
    ]

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name='notas'
    )

    autor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    fecha = models.DateTimeField(auto_now_add=True)

    evolucion = models.CharField(
        max_length=1,
        choices=EVOLUCION_CHOICES
    )

    diagnostico = models.TextField()

    glasgow = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(3), MaxValueValidator(15)]
    )

    escala_dolor = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    posicion_paciente = models.CharField(max_length=50)
    cambio_panal = models.CharField(max_length=50)

    tension_arterial = models.CharField(max_length=10)
    frecuencia_cardiaca = models.PositiveSmallIntegerField()
    frecuencia_respiratoria = models.PositiveSmallIntegerField()

    saturacion_oxigeno = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    temperatura = models.DecimalField(
        max_digits=4,
        decimal_places=1
    )

    procedimientos = models.TextField()

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f"Nota {self.get_evolucion_display()} - {self.paciente.nombres}"


class Adjunto(models.Model):

    nota = models.ForeignKey(
        NotaEnfermeria,
        on_delete=models.CASCADE,
        related_name='adjuntos'
    )

    archivo = models.FileField(upload_to='adjuntos/')
    descripcion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Adjunto - Nota {self.nota.id}"