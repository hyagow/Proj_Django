from django.forms import ModelForm
from .models import Transacao

class TransacaoForm(ModelForm):
    # Classe de metadata que recebe um model e os fields que queremos que sejam mostrados
    class Meta:
        model = Transacao
        fields = ['data', 'descricao', 'valor', 'observacoes', 'categoria']  # Com isto definiu-se um form que o Django vai criar todas as facilidades
        # Agora, precisa adicionar este import em views.py: from .form import TransacaoForm