
from rest_framework import viewsets
from estoque.api.serializers import Estoques
from .serializers import EstoqueSerializer

class EstoqueViewSet(viewsets.ModelViewSet):

    serializer_class = EstoqueSerializer

    def get_queryset(self):
        codproduto  = self.request.query_params.get('codproduto',None)

        queryset =Estoques.objects.all()
        if codproduto:
            queryset = codproduto.objects.filter(codproduto=codproduto)

        return queryset