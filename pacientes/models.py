from django.db import models
from django.contrib.auth.models import User


class Paciente(models.Model):
    nombre = models.CharField(max_length=200)
    documento = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ({self.documento})"


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
        on_delete=models.PROTECT
    )

    fecha = models.DateTimeField(auto_now_add=True)

    evolucion = models.CharField(
        max_length=1,
        choices=EVOLUCION_CHOICES
    )

    diagnostico = models.TextField()
    glasgow = models.PositiveSmallIntegerField()
    posicion_paciente = models.CharField(max_length=50)
    escala_dolor = models.PositiveSmallIntegerField()
    cambio_panal = models.CharField(max_length=50)

    tension_arterial = models.CharField(max_length=10)
    frecuencia_cardiaca = models.PositiveSmallIntegerField()
    saturacion_oxigeno = models.PositiveSmallIntegerField()
    frecuencia_respiratoria = models.PositiveSmallIntegerField()
    temperatura = models.DecimalField(max_digits=4, decimal_places=1)

    procedimientos = models.TextField()

    def __str__(self):
        return f"Nota {self.get_evolucion_display()} - {self.paciente.nombre}"


class Adjunto(models.Model):
    nota = models.ForeignKey(
        NotaEnfermeria,
        on_delete=models.CASCADE,
        related_name='adjuntos'
    )

    archivo = models.FileField(
        upload_to='adjuntos/'
    )

    descripcion = models.CharField(
        max_length=255,
        blank=True
    )

    def __str__(self):
        return f"Adjunto - Nota {self.nota.id}"


