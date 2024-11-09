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
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.template.loader import render_to_string

from books import models


class EnviarEmailView(APIView):
  def post(self, request):
        # Obter os dados da requisição
        destinatario = request.data.get('destinatario')
        nome = request.data.get('nome')
        assunto = request.data.get('assunto')
        mensagem = request.data.get('mensagem')

        # Contexto para o template
        context = {
            'nome': nome,
            'assunto': assunto,
            'mensagem': mensagem
        }

        # Renderizando o corpo do e-mail com o template HTML
        corpo_html = render_to_string('email_template.html', context)

        # Se quiser também enviar uma versão de texto simples, renderize o template de texto
        #corpo_texto = render_to_string('email_template.txt', context)

        try:
            # Enviar e-mail com HTML e versão texto
            send_mail(
                assunto,  # Assunto
                corpo_html,  # Corpo do e-mail em texto simples
                settings.EMAIL_HOST_USER,  # Remetente
                [destinatario],  # Destinatário(s)
                fail_silently=False,  # Lançar erro se falhar
                html_message=corpo_html  # Corpo do e-mail em HTML
            )
            return Response({"message": "E-mail enviado com sucesso!"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"Erro ao enviar e-mail: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



def json_teste(request):
    url = 'http://appexpressomoto2.ddns.net:8000/v1/entregas'
    headers={'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    response = json.loads(response.content)

    resultado = response

    context = {}
    context['resultado'] = resultado

    return render(request, 'base_principal.html', context)


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














