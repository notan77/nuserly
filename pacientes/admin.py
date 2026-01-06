from django.contrib import admin
from django import forms
from .models import Paciente, NotaEnfermeria, Adjunto


# ================================
# Personalización del Admin
# ================================
admin.site.site_header = "Nuserly System 1.0"
admin.site.site_title = "Nuserly Admin"
admin.site.index_title = "Panel de administración"


# ================================
# Formulario Paciente
# ================================
class PacienteAdminForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        required=False,
        widget=forms.SelectDateWidget(
            years=range(1920, 2031)
        )
    )

    class Meta:
        model = Paciente
        fields = "__all__"


# ================================
# Admin Paciente
# ================================
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    form = PacienteAdminForm
    list_display = ("nombres", "apellidos", "documento", "edad")
    search_fields = ("nombres", "apellidos", "documento")
    list_filter = ("sexo",)


# ================================
# Admin Nota Enfermería (INMUTABLE)
# ================================
@admin.register(NotaEnfermeria)
class NotaEnfermeriaAdmin(admin.ModelAdmin):
    list_display = ("paciente", "evolucion", "fecha", "autor")
    list_filter = ("evolucion", "fecha")
    search_fields = ("paciente__nombres", "paciente__apellidos")

    readonly_fields = (
        "paciente",
        "autor",
        "fecha",
        "evolucion",
        "diagnostico",
        "glasgow",
        "escala_dolor",
        "posicion_paciente",
        "cambio_panal",
        "tension_arterial",
        "frecuencia_cardiaca",
        "frecuencia_respiratoria",
        "saturacion_oxigeno",
        "temperatura",
        "procedimientos",
    )

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# ================================
# Admin Adjuntos
# ================================
@admin.register(Adjunto)
class AdjuntoAdmin(admin.ModelAdmin):
    list_display = ("nota", "archivo")
