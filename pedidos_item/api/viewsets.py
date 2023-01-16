
from rest_framework import viewsets
from pedidos_item.api.serializers import Itempedidos
from .serializers import Item_pedidos_Serializer

class Item_pedidos_ViewSet(viewsets.ModelViewSet):

    serializer_class = Item_pedidos_Serializer

    def get_queryset(self):
       # codpedido= self.request.query_params.get('codpedido')
        queryset =Itempedidos.objects.all()
        #if codpedido:
         #   queryset = queryset.filter(codpedido=codpedido)


        return queryset