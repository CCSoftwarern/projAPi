"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from books.api import viewsets as booksviewsets
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token
from books.views import CustomAuthToken

from books.views import AddEntregas, cadastrar_usuario, deleterEntrega, index, logar_usuario

route = routers.DefaultRouter(trailing_slash=False)
route.register(r'books', booksviewsets.BooksViewSet, basename="books")
route.register(r'empresa', booksviewsets.EmpresaViewSet, basename="empresa")
route.register(r'entregas', booksviewsets.EntregasViewSet, basename="entregas")
route.register(r'clientes', booksviewsets.ClientesViewSet, basename="clientes")
route.register(r'produtos', booksviewsets.ProdutosViewSet, basename="produtos")
route.register(r'formapgto', booksviewsets.FormaPgtoViewSet, basename="formapgto")
route.register(r'motoboys', booksviewsets.MotoboysViewSet, basename="motoboys")
route.register(r'users', booksviewsets.UserViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/',include(route.urls)),
    path('index', index, name="index"),
    path('', logar_usuario, name="logar_usuario"),
    path('cadastrar_usuario', cadastrar_usuario, name="cadastrar_usuario"),
    path('demo',TemplateView.as_view(template_name="bootstrap_base.html"),name='demo'),
    path('popovers',TemplateView.as_view(template_name="bootstrap_popovers.html"), name="popovers"),
    path('login',auth_views.LoginView.as_view(), name="login"),
    path('novaentrega',AddEntregas, name="novaentrega"),
    path('deletarentrega/<int:ID>',deleterEntrega, name="deletarentrega"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('rest_authtoken.urls')),
    path('v1/api-token-auth', obtain_auth_token, name='api_token_auth'),
    path('v1/detalhe/api-token-auth', CustomAuthToken.as_view())

]
