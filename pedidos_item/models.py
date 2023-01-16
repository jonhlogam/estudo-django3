from django.db import models
from pedidos.models import Pedidos_model


class Itempedidos(models.Model):

    codpedido = models.ForeignKey(Pedidos_model,blank=True, on_delete=models.CASCADE)
    codproduto = models.TextField(max_length=10, default=None)
    itemvalor = models.FloatField( null=True,blank=True)
    itemquantidade= models.IntegerField(blank=True)
    numseq= models.IntegerField(blank=True)
    date = models.DateTimeField(auto_now=True)
    status = models.TextField(max_length=1, default=None)

    def __str__(self):
        return self.codpedido


from django.db import models

# Create your models here.(
