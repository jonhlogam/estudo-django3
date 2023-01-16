
from rest_framework import viewsets
from produtos.api.serializers import Produto
from .serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):

    #queryset = Produto.objects.filter(destaque=True)
    serializer_class = ProdutoSerializer
    def get_queryset(self):
        codproduto = self.request.query_params.get('codproduto',None)
        codtabela  = self.request.query_params.get('codtabela',None)
        destaque   = self.request.query_params.get('destaque',None)
        queryset =Produto.objects.all()
        if codproduto:
            queryset = Produto.objects.filter(codproduto=codproduto)
        if codtabela:
            queryset =queryset.filter(codtabela=codtabela)
        if destaque:
            queryset =queryset.filter(destaque=destaque)

        return queryset

    ##def create(self, request, *args, **kwargs):
      #  pass