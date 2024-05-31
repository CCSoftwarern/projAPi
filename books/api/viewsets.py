from warnings import filters
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from books.api import serializers
from books import models
from django.contrib.auth.models import User
from django_filters import rest_framework as filters



class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializer
    queryset = models.Books.objects.all()


class EmpresaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmpresaSerializer
    queryset = models.Empresa.objects.all()


class MetricFilter(filters.FilterSet):
    DATA_DE_CADASTRO = filters.DateFromToRangeFilter()
    search_fields =['STATUS','DT_CADASTRO','ID','ID_MOTOQUEIRO','ID_PESSOA']

    class Meta:
        model = models.Entregas
        fields = ['STATUS','DT_CADASTRO','ID','ID_MOTOQUEIRO','ID_PESSOA'] 


class EntregasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EntregasSerializer
    queryset = models.Entregas.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = MetricFilter
    

class ClientesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClientesSerializer
    queryset = models.Clientes.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['NOME','CELULAR']
    search_fields = ['NOME', 'CELULAR']

class ProdutosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProdutosSerializer
    queryset = models.Produtos.objects.all()

class FormaPgtoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FormaPgtoSerializer
    queryset = models.FormaPgto.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ID','STATUS']

class MotoboysViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MotoboysSerializer
    queryset = models.Motoboys.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ONLINE']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username','is_staff']



