from pedidos_item.models import Itempedidos
from rest_framework import serializers


class Item_pedidos_Serializer (serializers.ModelSerializer):
    class Meta:
        model = Itempedidos
        fields= [
            'id',
        'codpedido',
        'codproduto',
        'itemvalor',
        'itemquantidade',
        'numseq',
        'date',
        'status'

        ]
