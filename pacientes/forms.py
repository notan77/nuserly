from django import forms
from .models import NotaEnfermeria


class NotaEnfermeriaForm(forms.ModelForm):

    class Meta:
        model = NotaEnfermeria
        exclude = ('autor', 'fecha', 'paciente')

        widgets = {
            'evolucion': forms.RadioSelect(),

            'diagnostico': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Diagnóstico del paciente'
            }),

            'procedimientos': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Procedimientos o actividades realizadas'
            }),

            'glasgow': forms.NumberInput(attrs={
                'min': 3,
                'max': 15
            }),

            'escala_dolor': forms.NumberInput(attrs={
                'min': 0,
                'max': 10
            }),

            'temperatura': forms.NumberInput(attrs={
                'step': '0.1'
            }),
        }
