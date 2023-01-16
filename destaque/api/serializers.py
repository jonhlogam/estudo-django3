from destaque.models import Destaque
from rest_framework import serializers

class DestaqueSerializer (serializers.ModelSerializer):
    class Meta:
        model = Destaque
        fields = [
            'codproduto',
            'nome',
            'descricao',
            'preco',
            'codtabela',
            'destaque',
            'imagem',
            'ft_venda',
            'unidade',
            'uni_master',
        ]
