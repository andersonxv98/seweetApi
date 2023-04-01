
from django.db import models
from djongo import  models as md
from djongo.models import ObjectIdField


# Create your models here.
class Pessoa(models.Model):
    atributo = models.CharField(max_length=50)


class ClienteCobranca(models.Model):
    p_pessoa = Pessoa.pk
    name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=13) # 55 18 99999 9999
    street = models.CharField(max_length=200)
    neighborhood = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=8)
    city = models.CharField(max_length=50)
    complement = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    value = models.IntegerField()
    expire_at = models.CharField(max_length=50)
    sigla = models.CharField(max_length=50)

class Autor(models.Model):
    id = ObjectIdField(primary_key=True)
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()

class Livros(models.Model):
    titulo =  models.CharField(max_length=50)
    nome_editora= models.CharField(max_length=50)
    teste = models.CharField(max_length=50)
    autor = md.EmbeddedField(model_container=Autor)
