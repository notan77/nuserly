from django.shortcuts import render, get_object_or_404
from .models import NotaEnfermeria


def imprimir_nota(request, nota_id):
    nota = get_object_or_404(NotaEnfermeria, id=nota_id)
    return render(request, "pacientes/imprimir_nota.html", {
        "nota": nota
    })

