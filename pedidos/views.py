from django.http import JsonResponse
from .models import Pedidos

def controle_pedidos(request):
    pedidos = Pedidos.objects.all().values()
    return JsonResponse(list(pedidos), safe = False)


def listar_pedidos_abertos(request):
    pedidos = Pedidos.objects.filter(status="ABERTO").values()
    return JsonResponse(list(pedidos), safe=False)

def listar_pedidos_em_preparo(request):
    pedidos = Pedidos.objects.filter(status="EM PREPARO").values()
    return JsonResponse(list(pedidos), safe=False)

def listar_pedidos_finalizados(request):
    pedidos = Pedidos.objects.filter(status="FINALIZADO").values()
    return JsonResponse(list(pedidos), safe=False)

def listar_pedidos_cancelados(request):
    pedidos = Pedidos.objects.filter(status="CANCELADO").values()
    return JsonResponse(list(pedidos), safe=False)