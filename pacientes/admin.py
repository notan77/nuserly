from django.contrib import admin
from django import forms
from .models import Paciente, NotaEnfermeria, Adjunto


# ==================================
# Personalización del Admin
# ==================================
admin.site.site_header = "Nuserly System 1.0"
admin.site.site_title = "Nuserly Admin"
admin.site.index_title = "Panel de administración"


# ==================================
# Formulario personalizado Paciente
# ==================================
class PacienteAdminForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        required=False,
        widget=forms.SelectDateWidget(
            years=range(1920, 2031)  # ajusta si quieres
        )
    )

    class Meta:
        model = Paciente
        fields = "__all__"


# ==================================
# Admin Paciente
# ==================================
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    form = PacienteAdminForm
    list_display = ("nombres", "apellidos", "documento", "edad")
    search_fields = ("nombres", "apellidos", "documento")
    list_filter = ("sexo",)


# ==================================
# Admin Nota Enfermería
# ==================================
@admin.register(NotaEnfermeria)
class NotaEnfermeriaAdmin(admin.ModelAdmin):
    list_display = ("paciente", "evolucion", "fecha", "autor")
    list_filter = ("evolucion", "fecha")
    search_fields = ("paciente__nombres", "paciente__apellidos")


# ==================================
# Admin Adjuntos
# ==================================
@admin.register(Adjunto)
class AdjuntoAdmin(admin.ModelAdmin):
    list_display = ("nota", "archivo")
