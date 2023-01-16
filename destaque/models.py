from django.db import models

def upload_imagem_produto(instance,filename):
    return f"{instance.codproduto}-{filename}"
def upload_imagem_banner(instance,filename):
    return f"{instance.cod_banner}-{filename}"
# Create your models here.

class Destaque(models.Model):


    codproduto = models.TextField()
    nome = models.TextField()
    descricao = models.TextField()
    preco = models.FloatField()
    codtabela = models.TextField()
    imagem=  models.ImageField()
    #image =  StdImageField('Imagem',upload_to=upload_imagem_produto,variations={'thumb':(150,150)})
    destaque = models.BooleanField()
    ft_venda= models.IntegerField()
    unidade=models.TextField()
    uni_master=models.TextField()

    class Meta:
        managed = False
        db_table = 'destaque_page'
    def __str__(self):
        return self.codproduto