from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    "Vista para renderizar la página inicial"
    return render(request, 'index.html')

def lista_usuarios(request):
    "Vista para renderizar la página donde se mostrarán los datos de usuarios"
    usuarios = User.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})