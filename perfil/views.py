from django.shortcuts import render
from .models import DatosPersonales, CursoRealizado, Reconocimientos, ProductosAcademicos, ProductoLaboral, VentaGarage, ExperienciaLaboral

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

def reconocimientos(request):
    datos = Reconocimientos.objects.all()  
    context = {'reconocimientos': datos}
    return render(request, 'reconocimientos.html', context)

def academico(request):
    datos = ProductosAcademicos.objects.all()
    context = {'academico': datos}
    return render(request, 'academico.html', context)

def laboral(request):
    productos = ProductoLaboral.objects.filter(activarparaqueseveaenfront=True)
    context = {
        'productolaboral': productos
    }
    return render(request, 'laboral.html', context)


def garage(request):
    # Solo los productos activados para mostrar
    productos = VentaGarage.objects.filter(activarparaqueseveaenfront=True)
    
    context = {
        'ventagarage': productos  # el nombre debe coincidir con el HTML
    }
    
    return render(request, 'garage.html', context)

def experiencia(request):
    datos = ExperienciaLaboral.objects.all()
    context = {'experiencias': datos}
    return render(request, 'experiencia.html', context)
