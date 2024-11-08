from rest_framework import serializers
from books import models
from django.contrib.auth.models import User



class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empresa
        fields = '__all__'


class EntregasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Entregas
        fields = '__all__'

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clientes
        fields = '__all__'

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Produtos
        fields = '__all__'

class FormaPgtoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FormaPgto
        fields = '__all__'
class MotoboysSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Motoboys
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff','id','token_push','url_imagem']

   



