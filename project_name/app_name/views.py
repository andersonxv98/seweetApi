"""from webbrowser import get

from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics"""
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import ClienteCobranca, Livros
"""from .serializers import ClienteCobrancaSerializer
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
# Create your views here."""
class ClienteCobrancaList(APIView):
    def get(self, request):
        get_data = request.query_params  # or request.GET check both
        print("REQUEST: ", get_data)
        filters = {}

        for key, value in get_data.items():
            if key in ['name', 'cpf',
                  'email','phone_number','street', 'neighborhood',
                  'zipcode', 'city', 'complement', 'state', 'value', 'expire_at', 'sigla']:
                filters[key] = value
        queryset = ClienteCobranca.objects.filter(**filters).values()
        return Response({"clientecobrancas" : queryset})
        #serializer_class = ClienteCobrancaSerializer

class LivrosList(APIView):
    def get(self, request):
        get_data = request.query_params  # or request.GET check both
        filters = {}

        for key, value in get_data.items():
            if key in ['titulo', 'nome_editora']:
                filters[key] = value
        queryset = Livros.objects.filter(**filters).values()
        return Response({"Livros" : queryset})