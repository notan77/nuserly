from django.urls import path
from .views import imprimir_nota

urlpatterns = [
    path("nota/<int:nota_id>/imprimir/", imprimir_nota, name="imprimir_nota"),
]
