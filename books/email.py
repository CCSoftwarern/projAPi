from django.core.mail import send_mail

def enviar_email(assunto, mensagem, destinatario):
    send_mail(
        assunto,
        mensagem,
        'ccsoftwarern@gmail.com',
        [destinatario],
        fail_silently=False,
    )
