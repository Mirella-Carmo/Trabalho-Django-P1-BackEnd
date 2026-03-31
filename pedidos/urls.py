from django.urls import path
from .views import controle_pedidos, listar_pedidos_abertos, listar_pedidos_cancelados, listar_pedidos_em_preparo, listar_pedidos_finalizados

urlpatterns = [
    path('pedidos/', controle_pedidos),
    path("pedidos/abertos/",listar_pedidos_abertos),
    path("pedidos/empreparo/", listar_pedidos_em_preparo),
    path("pedidos/finalizados/", listar_pedidos_finalizados),
    path("pedidos/cancelados/", listar_pedidos_cancelados)
]