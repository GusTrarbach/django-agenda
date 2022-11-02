from contatos.models import Contato
from django import forms


class FormContato(forms.ModelForm):
    """Classe de formulário"""

    class Meta:
        """Classe principal"""

        model = Contato
        exclude = ("mostrar",)
