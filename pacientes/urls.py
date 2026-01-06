from django.urls import path
from .views import home, crear_nota, imprimir_nota

urlpatterns = [
    path("", home, name="home"),
    path("paciente/<int:paciente_id>/nueva-nota/", crear_nota, name="crear_nota"),
    path("nota/<int:nota_id>/imprimir/", imprimir_nota, name="imprimir_nota"),
]
