from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Paciente, NotaEnfermeria
from .forms import NotaEnfermeriaForm


# ─────────────────────────────
# Home simple (temporal)
# ─────────────────────────────
@login_required
def home(request):
    pacientes = Paciente.objects.all()
    return render(request, "pacientes/home.html", {
        "pacientes": pacientes
    })


# ─────────────────────────────
# Crear nota de enfermería
# ─────────────────────────────
@login_required
def crear_nota(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == 'POST':
        form = NotaEnfermeriaForm(request.POST)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.paciente = paciente
            nota.autor = request.user
            nota.save()
            return redirect("home")
    else:
        form = NotaEnfermeriaForm()

    return render(request, "pacientes/crear_nota.html", {
        "form": form,
        "paciente": paciente
    })


# ─────────────────────────────
# Imprimir nota
# ─────────────────────────────
@login_required
def imprimir_nota(request, nota_id):
    nota = get_object_or_404(NotaEnfermeria, id=nota_id)
    return render(request, "pacientes/imprimir_nota.html", {
        "nota": nota
    })


