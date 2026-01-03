from django.shortcuts import render
from .models import DatosPersonales

def home(request):
    perfil = DatosPersonales.objects.first()  # Toma el primer perfil que tengas
    context = {
        'perfil': perfil
    }
    return render(request, 'home.html', context)

