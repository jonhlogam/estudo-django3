
from rest_framework import viewsets
from meta_gestores.api.serializers import Metas_gestores
from .serializers import Metas_Gestores_Serializer

class Metas_Gestores_ViewSet(viewsets.ModelViewSet):


    queryset = Metas_gestores.objects.all()
    serializer_class = Metas_Gestores_Serializer