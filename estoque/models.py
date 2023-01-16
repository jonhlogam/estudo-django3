from django.db import models


class Estoques(models.Model):


    codproduto = models.TextField(max_length=10, default=None)
    destaque = models.BooleanField(default=False)
    saldo= models.IntegerField(default=0,null=True)



    def __str__(self):
        return self.codproduto


from django.db import models

# Create your models here.
