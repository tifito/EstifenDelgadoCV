from django.shortcuts import render
from .models import DatosPersonales, CursoRealizado

def home(request):
    perfil = DatosPersonales.objects.first()  # Toma el primer perfil que tengas
    context = {
        'perfil': perfil
    }
    return render(request, 'home.html', context)

def cursos(request):
    cursos = CursoRealizado.objects.filter(activarparaqueseveaenfront=True)
    context = {
        'cursos': cursos
    }
    return render(request, 'cursos.html', context)