"""from .models import ClienteCobranca, Livros, Autor
from rest_framework import serializers
class ClienteCobrancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteCobranca
        fields = ['name', 'cpf',
                  'email','phone_number','street', 'neighborhood',
                  'zipcode', 'city', 'complement', 'state', 'value', 'expire_at', 'sigla']"""

"""class LivrosSerializer(serializers.ModelSerializer):
    autor = serializers.StringRelatedField(many=True)
    class Meta:
        model = Livros
        fields = ['id',{"autor" : {'nome': '', 'idade': ''}},'titulo', 'nome_editora']"""