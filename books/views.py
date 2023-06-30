from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from books import models
from books.api import serializers
from rest_framework.filters import SearchFilter

class ProductList(ListAPIView):
    queryset = models.FormaPgto.objects.all()
    serializer_class = serializers.FormaPgtoSerializer
    filter_backends = [SearchFilter]
    filterset_fields = ['ID', 'DESCRICAO']