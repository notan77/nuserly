from django.contrib import admin
from django import forms
from django.urls import reverse
from django.utils.html import format_html

from .models import Paciente, NotaEnfermeria, Adjunto


# ================================
# Branding Admin
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
# Inline Adjuntos (solo lectura)
# ================================
class AdjuntoInline(admin.TabularInline):
    model = Adjunto
    extra = 0
    can_delete = False
    readonly_fields = ("archivo", "descripcion")


# ================================
# Admin Nota Enfermería
# ================================
@admin.register(NotaEnfermeria)
class NotaEnfermeriaAdmin(admin.ModelAdmin):
    list_display = (
        "paciente",
        "evolucion",
        "fecha",
        "autor",
        "imprimir",
    )

    list_filter = ("evolucion", "fecha")
    search_fields = (
        "paciente__nombres",
        "paciente__apellidos",
        "paciente__documento",
    )

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

    inlines = [AdjuntoInline]

    # ─────────────
    # Botón imprimir (CORRECTO)
    # ─────────────
    @admin.display(description="Imprimir")
    def imprimir(self, obj):
        url = reverse("imprimir_nota", args=[obj.id])
        return format_html(
            '<a href="{}" target="_blank">🖨️ Imprimir</a>',
            url
        )

    # ─────────────
    # Seguridad clínica
    # ─────────────
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.autor = request.user
        super().save_model(request, obj, form, change)


# ================================
# Admin Adjuntos
# ================================
@admin.register(Adjunto)
class AdjuntoAdmin(admin.ModelAdmin):
    list_display = ("nota", "archivo")
