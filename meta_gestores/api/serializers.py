from meta_gestores.models import Metas_gestores
from rest_framework import serializers


class Metas_Gestores_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Metas_gestores
        fields = [
            'cod_equipe',
            'nome_equipe',
            'meta_equipe',
            'meta_master',
            'meta_forn',
            'cod_superv',
        ]
