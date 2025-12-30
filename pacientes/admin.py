from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Paciente, NotaEnfermeria, Adjunto


# ─────────────────────────────
# Branding del Admin (GLOBAL)
# ─────────────────────────────
admin.site.site_header = "Nuserly System 1.0"
admin.site.site_title = "Nuserly Admin"
admin.site.index_title = "Panel de Administración"


# ─────────────────────────────
# Inline de adjuntos (dentro de la nota)
# ─────────────────────────────
class AdjuntoInline(admin.TabularInline):
    model = Adjunto
    extra = 1


# ─────────────────────────────
# Admin de Nota de Enfermería
# ─────────────────────────────
@admin.register(NotaEnfermeria)
class NotaEnfermeriaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'autor', 'fecha', 'imprimir')
    readonly_fields = ('autor', 'fecha')
    inlines = [AdjuntoInline]

    def imprimir(self, obj):
        url = reverse('imprimir_nota', args=[obj.id])
        return format_html(
            '<a href="{}" target="_blank">🖨️ Imprimir</a>',
            url
        )
    imprimir.short_description = "Imprimir"

    # No permitir editar una nota ya creada
    def has_change_permission(self, request, obj=None):
        if obj:
            return False
        return super().has_change_permission(request, obj)

    # No permitir borrar notas
    def has_delete_permission(self, request, obj=None):
        return False

    # Asignar automáticamente el autor
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.autor = request.user
        super().save_model(request, obj, form, change)


# ─────────────────────────────
# Inline de notas dentro del paciente
# ─────────────────────────────
class NotaEnfermeriaInline(admin.TabularInline):
    model = NotaEnfermeria
    extra = 0
    readonly_fields = ('autor', 'fecha')
    can_delete = False


# ─────────────────────────────
# Admin de Paciente
# ─────────────────────────────
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'documento')
    search_fields = ('nombre', 'documento')
    inlines = [NotaEnfermeriaInline]
