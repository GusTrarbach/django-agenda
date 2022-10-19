from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404
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


def ver_contato(request, contato_id: int):
    """View para exibir a descrição dos contatos."""
    contato_obj = get_object_or_404(Contato, id=contato_id)

    if not contato_obj.mostrar:
        raise Http404()

    return render(request, "contatos/ver_contato.html", {"contato": contato_obj})
