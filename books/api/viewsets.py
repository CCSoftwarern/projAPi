from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from books.api import serializers
from books import models

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializer
    queryset = models.Books.objects.all()


class EmpresaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmpresaSerializer
    queryset = models.Empresa.objects.all()

class EntregasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EntregasSerializer
    queryset = models.Entregas.objects.all()

class ClientesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClientesSerializer
    queryset = models.Clientes.objects.all()

class ProdutosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProdutosSerializer
    queryset = models.Produtos.objects.all()

class FormaPgtoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FormaPgtoSerializer
    queryset = models.FormaPgto.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ID','DESCRICAO']

class MotoboysViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MotoboysSerializer
    queryset = models.Motoboys.objects.all()



