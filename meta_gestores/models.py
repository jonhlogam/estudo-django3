from django.db import models


class Metas_gestores(models.Model):
    cod_equipe = models.TextField(max_length=10, default=None, primary_key=True)
    nome_equipe = models.TextField(max_length=50, default=None)
    meta_equipe = models.FloatField(max_length=12, default=None)
    meta_master = models.FloatField(max_length=12, default=None)
    meta_forn = models.FloatField(max_length=12, default=None)
    cod_superv = models.IntegerField(default=None)


from django.db import models

# Create your models here.
