from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Value
from django.db.models.functions import Concat
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .models import Contato


# Create your views here.
def index(request):
    """View para a página principal."""
    all_contatos = Contato.objects.order_by("id").filter(mostrar=True)

    paginator = Paginator(all_contatos, 3)
    page = request.GET.get("p")
    all_contatos = paginator.get_page(page)

    return render(request, "contatos/index.html", {"contatos": all_contatos})


def busca(request):
    """View para a o resultado da busca na página principal."""
    termo = request.GET.get("termo")

    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, "Campo termo não pode ficar vazio")
        return redirect("index")

    campos = Concat("nome", Value(" "), "sobrenome")

    all_contatos = Contato.objects.annotate(nome_completo=campos).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo), mostrar=True
    )

    paginator = Paginator(all_contatos, 3)
    page = request.GET.get("p")
    all_contatos = paginator.get_page(page)

    return render(request, "contatos/busca.html", {"contatos": all_contatos})


def ver_contato(request, contato_id: int):
    """View para exibir a descrição dos contatos."""
    contato_obj = get_object_or_404(Contato, id=contato_id)

    if not contato_obj.mostrar:
        messages.add_message(request, messages.WARNING, "Esse contato não está disponível")
        return redirect("index")

    return render(request, "contatos/ver_contato.html", {"contato": contato_obj})
