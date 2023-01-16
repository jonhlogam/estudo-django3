from django.db import models

#from pedidos_item.models import Itempedidos


class Pedidos_model(models.Model):


    codpedido = models.TextField(primary_key=True,auto_created=True)
    cliente = models.TextField(max_length=10, default=None)
    codtabela = models.TextField(max_length=2, default=None)
    codpagamento = models.TextField(max_length=10, default=None)
    valortotal = models.FloatField(max_length=10, default=None)
    codtabela = models.TextField(max_length=2, default=None)
    prazo=models.TextField(max_length=10,null=True)
    rca=models.TextField(max_length=10, default=None)
    status=models.IntegerField(default=0)
    processado=models.BooleanField(default=False)
    #date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.codpedido

