from django.contrib import admin
from .models import Paciente, NotaEnfermeria, Adjunto


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ("nombres", "apellidos", "documento", "edad")
    search_fields = ("nombres", "apellidos", "documento")
    list_filter = ("sexo",)


@admin.register(NotaEnfermeria)
class NotaEnfermeriaAdmin(admin.ModelAdmin):
    list_display = ("paciente", "evolucion", "fecha", "autor")
    list_filter = ("evolucion", "fecha")
    search_fields = ("paciente__nombres", "paciente__apellidos")


@admin.register(Adjunto)
class AdjuntoAdmin(admin.ModelAdmin):
    list_display = ("nota", "archivo")
