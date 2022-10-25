from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    """Modelo para criação de categorias."""

    nome = models.CharField(max_length=255)

    def __str__(self) -> str:
        """Exibição na tabela admin das categorias.

        Somente é valido quando não se possui classe determinante no arquivo de admin
        """
        return self.nome


class Contato(models.Model):
    """Modelo para criação de contatos."""

    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=14)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to="fotos/%Y/%m")
