
from rest_framework import viewsets
from destaque.api.serializers import Destaque
from .serializers import DestaqueSerializer

class DestaqueViewSet(viewsets.ModelViewSet):

    #queryset = Produto.objects.filter(destaque=True)
    serializer_class = DestaqueSerializer
    def get_queryset(self):
        codproduto = self.request.query_params.get('codproduto',None)
        codtabela  = self.request.query_params.get('codtabela',None)
        destaque   = self.request.query_params.get('destaque',None)
        queryset =Destaque.objects.all()
        if codproduto:
            queryset = Destaque.objects.filter(codproduto=codproduto)
        if codtabela:
            queryset =queryset.filter(codtabela=codtabela)
        if destaque:
            queryset =queryset.filter(destaque=destaque)

        return queryset

    ##def create(self, request, *args, **kwargs):
      #  pass