from django import forms

from .models import Entregas

class EntregasForm(forms.ModelForm):

    class Meta:
        model = Entregas (Entregas.NM_CLIENTE, Entregas.ID_FORMA_PGTO, Entregas.VR_CALCULADO, Entregas.ENDERECO_RETIRADA, Entregas.ENDERECO_ENTREGA
                          , Entregas.ANOTACAO)
