from django.db import models
from django.contrib.auth.models import User


class Paciente(models.Model):
    nombre = models.CharField(max_length=200)
    documento = models.CharField(max_length=50, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.documento})"


class NotaEnfermeria(models.Model):
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name="notas"
    )
    autor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        editable=False
    )
    fecha = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f"Nota {self.fecha.strftime('%Y-%m-%d %H:%M')} - {self.paciente}"


class Adjunto(models.Model):
    nota = models.ForeignKey(
        NotaEnfermeria,
        on_delete=models.CASCADE,
        related_name="adjuntos"
    )
    archivo = models.FileField(upload_to="adjuntos/")
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Adjunto para {self.nota}"


