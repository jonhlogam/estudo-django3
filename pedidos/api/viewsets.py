
from rest_framework import viewsets
from pedidos.api.serializers import Pedidos_model
from .serializers import PedidoSerializer

class PedidosViewSet(viewsets.ModelViewSet):

    serializer_class = PedidoSerializer
    filterset_fields = ['codtabela', 'status']
    def get_queryset(self):
     #   cliente = self.request.query_params.get('cliente',None)
     #   status  = self.request.query_params.get('status',None)
     #   processado   = self.request.query_params.get('processado',None)
        queryset = Pedidos_model.objects.all()
        #if cliente:
        #    queryset = Pedidos_model.objects.filter(cliente=cliente)
       ## if status:
       #     queryset =queryset.filter(status=status)
       # if processado:
      #      queryset =queryset.filter(processado=processado)

        return queryset