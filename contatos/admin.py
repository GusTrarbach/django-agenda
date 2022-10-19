from typing import Sequence

from django.contrib import admin

from .models import Categoria
from .models import Contato


class ContatoAdmin(admin.ModelAdmin):
    """Classe responsável por editar característica de exibição do modelo na página de admin."""

    list_display: tuple = ("id", "nome", "sobrenome", "telefone", "email", "categoria", "mostrar")
    list_display_links: tuple = ("id", "nome", "sobrenome")
    list_filter: tuple = ("categoria",)
    list_per_page: int = 10
    search_fields: tuple[str] = ("nome", "sobrenome")
    list_editable: Sequence[str] = ("telefone", "mostrar")


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
