from banner.models import Banner
from rest_framework import serializers



class BannerSerializer (serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = [
            'cod_banner',
            'nome_banner',
            'descricao_banner',
            'image_banner'
                ]