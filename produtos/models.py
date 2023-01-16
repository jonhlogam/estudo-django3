from django.db import models

def upload_imagem_produto(instance,filename):
    return f"{instance.codproduto}-{filename}"
def upload_imagem_banner(instance,filename):
    return f"{instance.cod_banner}-{filename}"
# Create your models here.

class Produto(models.Model):


    codproduto = models.TextField(max_length=10, default=None)
    nome = models.TextField(max_length=100, default=None)
    descricao = models.TextField(max_length=100, default=None)
    preco = models.FloatField(max_length=100, default=None)
    codtabela = models.TextField(max_length=2, default=None)
    imagem=  models.ImageField(upload_to=upload_imagem_produto, blank=True,null=True)
    #image =  StdImageField('Imagem',upload_to=upload_imagem_produto,variations={'thumb':(150,150)})
    destaque = models.BooleanField(default=False)
    ft_venda= models.IntegerField(default=1,null=True)
    unidade=models.TextField(max_length=2,null=True)
    uni_master=models.TextField(max_length=2,null=True)

    def __str__(self):
        return self.codproduto