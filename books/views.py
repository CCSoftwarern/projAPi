import json, requests
from pdb import post_mortem
from typing import Generic
from urllib.request import Request
from warnings import filters
from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Entregas
from django.template import loader
from django.contrib import messages
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from books import models

# Create your views here.

def json_teste(request):
    url = 'http://appexpressomoto2.ddns.net:8000/v1/entregas'
    headers={'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    response = json.loads(response.content)

    resultado = response

    context = {}
    context['resultado'] = resultado

    return render(request, 'entregas.html', context)


def my_view(request):
    data = models.objects.all().values()
    json_data = json.dumps(list(data))
    return HttpResponse(json_data, content_type='application/json')

    
    

def index(request):
  #mydata = Member.objects.filter(firstname='Emil').values()
  #myindex = Entregas.objects.all().values()
  myindex = Entregas.objects.filter(STATUS='P').values()
  template = loader.get_template('base_principal.html')
  context = {
    'myindex': myindex,
  }
  return HttpResponse(template.render(context, request))

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('confirmacao')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'cadastro.html', {'form_usuario': form_usuario})


# LOGAR USUARIO
def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})

# INICIO GRAVAR ENTREGA

def AddEntregas(request):
    novaentrega = Entregas()
    novaentrega.NM_CLIENTE = request.POST.get('nome_cliente')
    novaentrega.ENDERECO_RETIRADA = request.POST.get('origem')
    novaentrega.ENDERECO_ENTREGA = request.POST.get('destino')
    novaentrega.save()
    return redirect('index')

def deleterEntrega(request, id):
    task = get_object_or_404(Entregas, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')

    return redirect('/')

# FIM GRAVAR ENTREGA

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'last_name': user.last_name,
            'first_name': user.first_name,
            'last_login': user.last_login,
            'is_staff': user.is_staff,
            'is_active': user.is_active,
            'token_push': user.token_push,
            'url_imagem': user.url_imagem

        })
    
def vconfirmacao(request): 
    # return response 
    return render(request, "confirmacao.html") 














