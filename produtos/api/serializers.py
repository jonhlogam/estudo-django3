from produtos.models import Produto
from rest_framework import serializers

class ProdutoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Produto
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
