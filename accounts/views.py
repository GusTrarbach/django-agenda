from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.shortcuts import redirect
from django.shortcuts import render


def login(request):
    """Tela de login"""
    return render(request, "accounts/login.html")


def logout(request):
    """Tela de logout"""
    return render(request, "accounts/logout.html")


def register(request):
    """Tela de registro"""
    if request.method != "POST":
        return render(request, "accounts/register.html")

    nome = request.POST.get("nome")
    sobrenome = request.POST.get("sobrenome")
    email = request.POST.get("email")
    usuario = request.POST.get("usuario")
    senha = request.POST.get("senha")
    senha2 = request.POST.get("senha2")

    form_info = [nome, sobrenome, email, usuario, senha, senha2]

    if not all(form_info):
        messages.error(request, "Nenhum campo pode estar vazio")
        return render(request, "accounts/register.html")

    try:
        validate_email(email)
    except Exception:
        messages.error(request, "E-mail inválido")
        return render(request, "accounts/register.html")

    if len(senha) < 6:
        messages.error(request, "Senha precisa ter ao menos 6 caracteres")
        return render(request, "accounts/register.html")

    if len(usuario) < 6:
        messages.error(request, "Usuário precisa ter pelo menos 6 caracteres")
        return render(request, "accounts/register.html")

    if senha != senha2:
        messages.error(request, "As senhas estão divergentes")
        return render(request, "accounts/register.html")

    if User.objects.filter(username=usuario).exists():
        messages.error(request, "Usuário já existe")
        return render(request, "accounts/register.html")

    if User.objects.filter(email=email).exists():
        messages.error(request, "E-mail já existe")
        return render(request, "accounts/register.html")

    messages.success(request, "Usuário registrado com sucesso.")

    user = User.objects.create_user(
        username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome
    )
    user.save()
    return redirect("login")


def dashboard(request):
    """Tela de dashboard"""
    return render(request, "accounts/dashboard.html")
