from django.urls import path
from .views import home, imprimir_nota

urlpatterns = [
    path("", home, name="home"),
    path("nota/<int:nota_id>/imprimir/", imprimir_nota, name="imprimir_nota"),
]
