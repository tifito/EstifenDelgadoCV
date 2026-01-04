from django.contrib import admin

# admin.py
# Por ahora no hay modelos, así que no hacemos nada aquí

from django.contrib import admin
from .models import (
    DatosPersonales, ExperienciaLaboral, Reconocimientos,
    CursoRealizado, ProductosAcademicos, ProductoLaboral, VentaGarage
)

@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'numerocedula', 'sitioweb')
    fields = (
        'descripcionperfil', 'perfilactivo', 'apellidos', 'nombres', 'nacionalidad',
        'lugarnacimiento', 'fechanacimiento', 'numerocedula', 'sexo', 'estadocivil',
        'licenciaconducir', 'telefonoconvencional', 'telefonofijo', 'direcciontrabajo',
        'direcciondomiciliaria', 'sitioweb', 'email', 'fotodeperfil',
    )

@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(admin.ModelAdmin):
    list_display = ('cargodesempenado', 'nombrempresa', 'fechainiciogestion', 'activarparaqueseveaenfront')
    list_filter = ('activarparaqueseveaenfront', 'nombrempresa')
    fields = (
        'perfil', 'cargodesempenado', 'nombrempresa', 'lugarempresa', 'emailempresa',
        'sitiowebempresa', 'nombrecontactoempresarial', 'telefonocontactoempresarial',
        'fechainiciogestion', 'fechafingestion', 'descripcionfunciones',
        'activarparaqueseveaenfront', 'rutacertificado'
    )

@admin.register(Reconocimientos)
class ReconocimientosAdmin(admin.ModelAdmin):
    list_display = ('descripcionreconocimiento', 'tiporeconocimiento', 'entidadpatrocinadora')
    list_filter = ('tiporeconocimiento',)
    fields = (
        'perfil', 'tiporeconocimiento', 'fechareconocimiento', 'descripcionreconocimiento',
        'entidadpatrocinadora', 'nombrecontactoauspicia', 'telefonocontactoauspicia',
        'activarparaqueseveaenfront', 'rutacertificado'
    )

@admin.register(CursoRealizado)
class CursoRealizadoAdmin(admin.ModelAdmin):
    list_display = ('nombrecurso', 'entidadpatrocinadora', 'totalhoras')
    fields = (
        'perfil', 'nombrecurso', 'fechainicio', 'fechafin', 'totalhoras', 'descripcioncurso',
        'entidadpatrocinadora', 'nombrecontactoauspicia', 'telefonocontactoauspicia',
        'emailempresapatrocinadora', 'activarparaqueseveaenfront', 'rutacertificado'
    )

@admin.register(ProductosAcademicos)
class ProductosAcademicosAdmin(admin.ModelAdmin):
    list_display = ('nombrerecurso', 'clasificador', 'activarparaqueseveaenfront')
    fields = (
        'perfil', 'nombrerecurso', 'clasificador', 'descripcion', 'activarparaqueseveaenfront', 'rutaproductoacademico',
    )

@admin.register(ProductoLaboral)
class ProductoLaboralAdmin(admin.ModelAdmin):
    list_display = ('nombreproducto', 'fechaproducto', 'activarparaqueseveaenfront')
    fields = (
        'perfil', 'nombreproducto', 'fechaproducto', 'descripcion', 'activarparaqueseveaenfront', 'rutaproductolaboral',
    )

@admin.register(VentaGarage)
class VentaGarageAdmin(admin.ModelAdmin):
    list_display = ('nombreproducto', 'valordelbien', 'estadoproducto', 'activarparaqueseveaenfront')
    list_filter = ('estadoproducto', 'activarparaqueseveaenfront')
    fields = (
        'perfil', 'nombreproducto', 'estadoproducto', 'descripcion', 'valordelbien',
        'activarparaqueseveaenfront', 'rutaproducto',
    )
