from django.db import models

def upload_imagem_banner(instance,filename):
    return f"{instance.cod_banner}-{filename}"

# Create your models here.
class Banner(models.Model):

    cod_banner = models.TextField(max_length=10, default=None,primary_key = True)
    nome_banner = models.TextField(max_length=100, default=None)
    descricao_banner = models.TextField(max_length=100, default=None)
    image_banner=  models.ImageField(upload_to=upload_imagem_banner, blank=True,null=True)

