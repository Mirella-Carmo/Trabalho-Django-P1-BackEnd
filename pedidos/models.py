from django.db import models

class Pedidos(models.Model):
    STATUS_CHOICE = [
        ("Aberto", "ABERTO"),
        ("Em Preparo", "EM PREPARO"),
        ("Finalizado", "FINALIZADO"),
        ("Cancelado", "CANCELADO")
    ]
    
    prato = models.CharField(max_length=100)
    mesa = models.IntegerField()
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=4, decimal_places=2)
    status = models.CharField(max_length=20, choices= STATUS_CHOICE, default= 'ABERTA')
    
    def __str__(self):
        return f'Pedido: {self.prato} Mesa: {self.mesa}' 