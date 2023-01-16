from pedidos.models import Pedidos_model
from rest_framework import serializers
from pedidos_item.api.serializers import Item_pedidos_Serializer

class PedidoSerializer (serializers.ModelSerializer):
    codpedido  = Item_pedidos_Serializer(many=True,read_only=True)

    class Meta:
        model = Pedidos_model
        fields= [
            'codpedido',
            'cliente' ,
            'codtabela',
            'codpagamento',
            'valortotal',
            'codtabela',
            'prazo',
            'rca',
            'status',
            'processado',

            #'date',

               ]