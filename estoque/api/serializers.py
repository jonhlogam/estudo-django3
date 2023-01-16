from estoque.models import Estoques
from rest_framework import serializers

class EstoqueSerializer (serializers.ModelSerializer):
    class Meta:
        model = Estoques
        fields= [
        'codproduto',
        'destaque',
        'saldo'
        ]
