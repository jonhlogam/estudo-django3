
from rest_framework import viewsets
from banner.api.serializers import Banner
from .serializers import BannerSerializer

class BannerViewSet(viewsets.ModelViewSet):


    #queryset = Produto.objects.filter(destaque=True)

    queryset = Banner.objects.all()
    serializer_class = BannerSerializer      #  pass