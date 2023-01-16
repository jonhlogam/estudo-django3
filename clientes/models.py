from django.db import models


class Cliente(models.Model):
    nome = models.TextField(max_length=100, default=None)
    cnpj = models.TextField(max_length=140, default=None,primary_key = True)
    senha = models.TextField(max_length=120,default=None)
    email = models.TextField(max_length=120, default=None)
    telefone = models.TextField(max_length=120, default=None)
    confirma_senha= models.TextField(max_length=120, default=None)
    status=models.BooleanField(default=False)
    codtabela= models.IntegerField(default=0)