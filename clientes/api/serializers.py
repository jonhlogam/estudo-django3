from clientes.models import Cliente
from rest_framework import serializers

class ClienteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields= ["nome",
                 "cnpj",
                 "senha",
                 "email",
                 "telefone",
                 "confirma_senha",
                 "status",
                 "codtabela"
                ]
