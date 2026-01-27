from django.shortcuts import render
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from .models import (
    DatosPersonales,
    CursoRealizado,
    Reconocimientos,
    ProductosAcademicos,
    ProductoLaboral,
    VentaGarage,
    ExperienciaLaboral
)

# -------------------------
# UTILIDAD
# -------------------------
def perfil_activo():
    perfil = DatosPersonales.objects.first()
    return perfil if perfil and perfil.perfilactivo else None


# -------------------------
# HOME
# -------------------------
def home(request):
    perfil = perfil_activo()
    return render(request, 'home.html', {'perfil': perfil})


# -------------------------
# CURSOS
# -------------------------
def cursos(request):
    perfil = perfil_activo()
    cursos = (
        CursoRealizado.objects
        .filter(activarparaqueseveaenfront=True)
        .order_by('-fechainicio')
        if perfil else None
    )
    return render(request, 'cursos.html', {
        'perfil': perfil,
        'cursos': cursos
    })



def reconocimientos(request):
    perfil = perfil_activo()
    datos = (
        Reconocimientos.objects
        .filter(activarparaqueseveaenfront=True)
        .order_by('-fechareconocimiento')
        if perfil else None
    )
    return render(request, 'reconocimientos.html', {
        'perfil': perfil,
        'reconocimientos': datos
    })


def academico(request):
    perfil = perfil_activo()
    datos = (
        ProductosAcademicos.objects
        .filter(activarparaqueseveaenfront=True)
        if perfil else None
    )
    return render(request, 'academico.html', {
        'perfil': perfil,
        'academico': datos
    })



def laboral(request):
    perfil = perfil_activo()
    productos = (
        ProductoLaboral.objects
        .filter(activarparaqueseveaenfront=True)
        .order_by('-fechaproducto')
        if perfil else None
    )
    return render(request, 'laboral.html', {
        'perfil': perfil,
        'productolaboral': productos
    })



def garage(request):
    perfil = perfil_activo()
    productos = (
        VentaGarage.objects
        .filter(activarparaqueseveaenfront=True)
        .order_by('-fechapublicacion')
        if perfil else None
    )
    return render(request, 'garage.html', {
        'perfil': perfil,
        'ventagarage': productos
    })



def experiencia(request):
    perfil = perfil_activo()
    datos = (
        ExperienciaLaboral.objects
        .filter(activarparaqueseveaenfront=True)
        .order_by('-fechainiciogestion')
        if perfil else None
    )
    return render(request, 'experiencia.html', {
        'perfil': perfil,
        'experiencias': datos
    })


def cv_pdf(request):
    perfil = perfil_activo()

    if not perfil:
        return HttpResponse("Perfil no disponible", status=404)

    mostrar_perfil = 'perfil' in request.GET
    mostrar_descripcion = 'descripcion' in request.GET
    mostrar_educacion = 'educacion' in request.GET
    mostrar_experiencia = 'experiencia' in request.GET
    mostrar_cursos = 'cursos' in request.GET
    mostrar_reconocimientos = 'reconocimientos' in request.GET
    mostrar_productos = 'productos' in request.GET

    context = {
        'perfil': perfil,

        # FLAGS PARA EL TEMPLATE
        'mostrar_perfil': mostrar_perfil,
        'mostrar_descripcion': mostrar_descripcion,
        'mostrar_educacion': mostrar_educacion,
        'mostrar_experiencia': mostrar_experiencia,
        'mostrar_cursos': mostrar_cursos,
        'mostrar_reconocimientos': mostrar_reconocimientos,
        'mostrar_productos': mostrar_productos,

        # DATA
        'academico': ProductosAcademicos.objects.filter(
            activarparaqueseveaenfront=True
        ),

        'cursos': CursoRealizado.objects.filter(
            activarparaqueseveaenfront=True
        ).order_by('-fechainicio'),

        'experiencias': ExperienciaLaboral.objects.filter(
            activarparaqueseveaenfront=True
        ).order_by('-fechainiciogestion'),

        'productos': ProductoLaboral.objects.filter(
            activarparaqueseveaenfront=True
        ).order_by('-fechaproducto'),

        'reconocimientos': Reconocimientos.objects.filter(
            activarparaqueseveaenfront=True
        ).order_by('-fechareconocimiento'),
    }

    template = get_template('cvpdf.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="cv.pdf"'

    pisa.CreatePDF(html, dest=response)

    return response
