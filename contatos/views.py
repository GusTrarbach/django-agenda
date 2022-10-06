from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Contato


# Create your views here.
def index(request):
    """View para a página principal."""
    all_contatos = Contato.objects.all()
    return render(request, "contatos/index.html", {"contatos": all_contatos})


def ver_contato(request, contato_id: int):
    """View para exibir a descrição dos contatos."""
    id_contato = get_object_or_404(Contato, id=contato_id)
    return render(request, "contatos/ver_contato.html", {"contato": id_contato})
