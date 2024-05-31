from django.db import models
from uuid import uuid4






# Create your models here.
class Books(models.Model):
    id_book = models.UUIDField(primary_key=True,default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)
  


class Empresa(models.Model):
    EMP_ID   =            models.UUIDField(primary_key=True,default=uuid4, editable=False)
    EMP_FANTASIA =         models.CharField(max_length=255)
    EMP_RAZAOSOCIAL  =     models.CharField(max_length=255)
    EMP_NOMEREDUZIDO   =   models.CharField(max_length=255)
    EMP_PESSOA    =        models.CharField(max_length=1, null=True)
    EMP_CPF      =         models.CharField(max_length=11, null=True)
    EMP_CNPJ     =         models.CharField(max_length=18, null=True)
    EMP_FONES       =       models.CharField(max_length=50, null=True)
    EMP_CONTATO     =       models.CharField(max_length=50, null=True)
    EMP_SITUACAO    =       models.CharField(max_length=1, null=True)
    EMP_OBSERVACAO   =      models.CharField(max_length=255, null=True)
    EMP_USUCAD     =        models.CharField(max_length=15, null=True)
    EMP_DATCAD     =       models.DateTimeField( null=True)
    EMP_USUMOD     =       models.CharField(max_length=15, null=True)
    EMP_DATMOD     =       models.DateTimeField( null=True)
    EMP_ATIVA       =      models.CharField(max_length=1, null=True)
    EMP_API_GOOGLE   =     models.CharField(max_length=255, null=True)
    EM_API_URL_BASE   =    models.CharField(max_length=255, null=True)
    EMP_API_PAGSEGURO   =  models.CharField(max_length=255, null=True)
    EMP_API_URL_BASE    =  models.CharField(max_length=255, null=True)
    EMP_VR_KM       =      models.FloatField( null=True)
    LIMITE_FIXO    =       models.IntegerField( null=True)
    STATUS         =       models.IntegerField(default=0)
    VR_LIMITE_FIXO   =     models.FloatField(default=0)
    EM_CEP          =      models.CharField(max_length=255, null=True)
    EMP_ENDERECO    =      models.CharField(max_length=255, null=True)
    EMP_BAIRRO      =      models.CharField(max_length=255, null=True)
    EMP_COMPLEMENTO   =    models.CharField(max_length=255, null=True)
    EMP_EMAIL         =    models.CharField(max_length=255, null=True)
    EMP_NUMERO    =        models.IntegerField(default=0)
    EMP_UF            =    models.CharField(max_length=2, null=True)
    EMP_CIDADE         =   models.CharField(max_length=255, null=True)
    EMP_TELEFONE        =  models.CharField(max_length=255, null=True)
    EMP_CELULAR         =  models.CharField(max_length=255, null=True)
    EMP_DT_FUNDACAO     =  models.DateField(null=True)
    EMP_INC_MUNICIPAL   =  models.CharField(max_length=255, null=True)
    EMP_INC_ESTADUAL   =   models.CharField(max_length=255, null=True)
    API_KEY_G          =   models.CharField(max_length=255, null=True)
    API_CNPJ           =   models.CharField(max_length=255, null=True)
    API_CEP            =   models.CharField(max_length=255, null=True)
    CHAVE_PIX          =   models.CharField(max_length=255, null=True)
    API_WATS               =models.CharField(max_length=255, null=True)
    API_WATS_BASE          =models.CharField(max_length=255, null=True)
    DIA_DE_FECHAMENTO =   models.IntegerField(default=0)
    INICIO_ATIVIDADES     = models.TimeField(null=True)
    FIM_ATIVIDADES    =     models.TimeField(null=True)
    URLGOOGLE         =    models.CharField(max_length=255, null=True)
    COD_PROJ_GOOGLE   =     models.CharField(max_length=255, null=True)
    API_GOOGLE         =    models.CharField(max_length=255, null=True)
    IMPRIMIR        =       models.IntegerField(default=0)
    IP_IMPRESSORA_TERMICA  = models.CharField(max_length=255, null=True)
    NM_IMPRESSORA          = models.CharField(max_length=255, null=True)

def upload_image_assinatura(instance, filename):
    return f"{instance.ID}-{filename}"

class Entregas(models.Model):   
    ID                  =        models.AutoField(primary_key=True,editable=False)
    ID_TIPO_PRODUTO      =      models.CharField(max_length=38, default=0)
    NM_PRODUTO          =       models.CharField(max_length=30, default="Não selecionado")
    ID_PESSOA           =      models.CharField(max_length=38, default=0)
    NM_PESSOA           =       models.CharField(max_length=200, default="Não selecionado")
    ID_MOTOQUEIRO       =      models.CharField(max_length=38, default=0)
    NM_MOTOQUEIRO       =      models.CharField(max_length=100, default="Não selecionado")
    DT_CADASTRO         =     models.DateField(auto_now_add=True)
    DT_SAIDA           =      models.DateField(null=True)
    DT_ENTREGA          =     models.DateTimeField(null=True)
    ENDERECO_RETIRADA          = models.CharField(max_length=600, null=True)
    ENDERECO_ENTREGA            = models.CharField(max_length=600, null=True)
    DESCRICAO                  = models.CharField(max_length=600, null=True)
    DISTANCIA            =      models.IntegerField(default=0, null=True)
    DISTANCIA_TXT               = models.CharField(max_length=30, null=True)
    VR_CALCULADO       =        models.FloatField(default=0, null=True)
    VR_POR_METRO      =         models.FloatField(default=0, null=True)
    STATUS                      = models.CharField(max_length=1, default="0")
    ID_FORMA_PGTO        =     models.CharField(max_length=38, default=0)
    NM_FORMA_PGTO       =       models.CharField(max_length=30, default="Não selecionado")
    ID_EMPRESA           =    models.CharField(max_length=38, default=0)
    ID_USUARIO_ENCERRAMENTO   =models.CharField(max_length=38, default=0)
    NM_USUARIO_ENCERRAMENTO   = models.CharField(max_length=200, default="Não informado")
    ID_USUARIO_INCLUSAO       = models.CharField(max_length=38, default=0)
    NM_USUARIO_ENCERRAMENTO   = models.CharField(max_length=200, default="Não informado")
    COD_TRANSACAO               = models.CharField(max_length=20, default=0)
    BAIRRO_ENTREGA              = models.CharField(max_length=255, default='Não informado')
    TRANSACAO_GUID              = models.CharField(max_length=38, default='Não informado')
    ENDERECO_CLIENTE            = models.CharField(max_length=600, default='Não informado')
    ANOTACAO                    = models.CharField(max_length=600, default='Não informado')
    ID_USUARIO_ENCAMINHAMENTO = models.CharField(max_length=38, default=0)
    NM_USUARIO_ENCERRAMENTO   = models.CharField(max_length=200, default="Não informado")
    TRANSFERIDO                 = models.IntegerField(default=0, null=True)
    NM_CLIENTE                  = models.CharField(max_length=255, default='Não informado')
    DATA_DE_CADASTRO           =models.DateTimeField(auto_now_add=True, null=True)
    DATA_DE_ENTREGA            =models.DateTimeField(auto_now_add=True, null=True)
    URL_IMAGEM                 =models.URLField(max_length=255, null=True, blank = True)
    IMG_ASSINATURA             = models.ImageField(upload_to=upload_image_assinatura, blank=True, null=True)
    NM_ATENDENTE               = models.CharField(max_length=200, default="Não informado")
<<<<<<< HEAD
    IMG_ASS_BASE64              = models.TextField(null=True)
=======
>>>>>>> a2b13ee167e27b3d7ff6a3b5c4c129550ac4b488

def upload_image_clientes(instance, filename):
    return f"{instance.IDPESSOA}-{filename}"

class Clientes(models.Model): 
    IDPESSOA           =  models.AutoField(primary_key=True,editable=False)
    NOME                = models.CharField(max_length=255)
    EMAIL               = models.CharField(max_length=255, null=True)
    CPF                 = models.CharField(max_length=20, null=True, unique=True)
    CELULAR             = models.CharField(max_length=20, null=True, unique=True)
    LATITUDE            = models.CharField(max_length=20, null=True)
    LONGITUDE           = models.CharField(max_length=20, null=True)
    ONLINE           = models.CharField(max_length=100, null=True)
    TOKEN               = models.CharField(max_length=255, null=True)
    SENHA                = models.CharField(max_length=10, null=True)
    STATUS               = models.CharField(max_length=1, null=True)
    TP_PESSOA            = models.CharField(max_length=1, null=True)
    DT_TIME_ONLINE     =   models.DateTimeField(auto_now_add=True)
    ENDERECO             = models.CharField(max_length=100, null=True)
    BAIRRO               = models.CharField(max_length=100, null=True)
    NUMERO           = models.CharField(max_length=100, null=True)
    COMPLEMENTO          = models.CharField(max_length=100, null=True)
    CEP                = models.CharField(max_length=9, null=True)
    ESTADO             = models.CharField(max_length=100, null=True)
    CIDADE             = models.CharField(max_length=100, null=True)
    TP_CPF_CNPJ     =    models.IntegerField(default=0, null=True)
    TEM_CONTRATO     =    models.IntegerField(default=0, null=True)
    ID_EMPRESA        =   models.IntegerField(default=0, null=True)
    ID_USUARIO        =   models.IntegerField(default=0, null=True)
    IDMOTOQUEIRO      =  models.IntegerField(default=0, null=True)
    TELEFONE_IMPORTADO  = models.CharField(max_length=100, null=True)
    PONTO_REFERENCIA    = models.CharField(max_length=100, null=True)
    OBS                = models.CharField(max_length=100, null=True)
    ID_IMPORTADO       =  models.IntegerField(default=0, null=True)
    NUMERO_IMPORTADO    = models.CharField(max_length=100, null=True)
    TOKEN_CELULAR       = models.CharField(max_length=255, null=True)
    ID_TABELA          =  models.IntegerField(default=0, null=True)
    IPCOOPERATIVA       = models.CharField(max_length=20, null=True)
    CHAVE_PIX           = models.CharField(max_length=100, null=True)
    TP_CHAVE           = models.CharField(max_length=100, null=True)
    CK_ATIVO            =models.BooleanField(null=True)
    ONLINE_2            =models.BooleanField(null=True)
    NR_CELULAR2         =models.BigIntegerField(null=True)
    FOTO = models.ImageField(upload_to=upload_image_clientes, blank=True, null=True)

class Produtos (models.Model):
    ID          =  models.AutoField(primary_key=True,editable=False)
    NM_PRODUTO    = models.CharField(max_length=100)
    DESC_PRODUTO    = models.CharField(max_length=600, null=True)
    TARIFA_P_METRO  = models.FloatField(default=0)
    KM_MINIMO      =  models.IntegerField(default=0)
    VR_KM_MINIMO   =  models.FloatField(default=0)
    STATUS          = models.CharField(max_length=1, default="0")
    ID_EMPRESA  = models.CharField(max_length=38, default=0)
    ATIVO_APP      = models.CharField(max_length=1, default="0")

class FormaPgto (models.Model):
    ID     =  models.AutoField(primary_key=True,editable=False)
    DESCRICAO   = models.CharField(max_length=100)
    STATUS      = models.CharField(max_length=1, default="0")
    ID_EMPRESA   =  models.CharField(max_length=38, default=0)


def upload_image_motoboy(instance, filename):
    return f"{instance.ID_MOTOBOY}-{filename}"
    
class Motoboys(models.Model):
    ID_MOTOBOY    =  models.AutoField(primary_key=True,editable=False)
    NOME    = models.CharField(max_length=255)
    CELULAR  = models.CharField(max_length=20, unique=True)
    TOKEN = models.CharField(max_length=255)
    ONLINE = models.CharField(max_length=1, default="0")
    FOTO = models.ImageField(upload_to=upload_image_motoboy, blank=True, null=True)
    ID_USER = models.IntegerField(default=0)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class MeusLocais(models.Model):
    ID              =models.AutoField(primary_key=True,editable=False)
    ID_PESSOA      =models.ForeignKey(Question, on_delete=models.CASCADE)
    ENDERECO       =models.CharField(max_length=255,null=True)
    APELIDO_LOCAL  =models.CharField(max_length=100,null=True)
    DT_CADASTRO    =models.DateTimeField(auto_now_add=True)
    VALOR         =models.FloatField( null=True)
    TP             =models.CharField(max_length=1,null=True)



