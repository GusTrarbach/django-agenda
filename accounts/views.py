from django.shortcuts import render


def login(request):
    """Tela de login"""
    return render(request, "accounts/login.html")


def logout(request):
    """Tela de logout"""
    return render(request, "accounts/logout.html")


def register(request):
    """Tela de registro"""
    return render(request, "accounts/register.html")


def dashboard(request):
    """Tela de dashboard"""
    return render(request, "accounts/dashboard.html")
