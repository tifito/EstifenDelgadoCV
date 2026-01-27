from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
from django.utils import timezone
from cloudinary.models import CloudinaryField



class DatosPersonales(models.Model):

    SOLO_LETRAS = RegexValidator(
        regex=r'^[a-zA-ZÁÉÍÓÚáéíóúÑñ\s]+$',
        message='Este campo solo debe contener letras.'
    )
    SOLO_NUMEROS = RegexValidator(
        regex=r'^[0-9]+$',
        message='Este campo solo debe contener números.'
    )

    ESTADO_CIVIL_CHOICES = [('Soltero','Soltero'),('Casado','Casado'),('Divorciado','Divorciado'),('Viudo','Viudo')]
    LICENCIA_CHOICES = [('Sí','Sí'),('No','No')]

    descripcionperfil = models.CharField(max_length=500)
    titulodescripcion = models.CharField(max_length=200)
    perfilactivo = models.BooleanField(default=True)
    apellidos = models.CharField(max_length=60, validators=[SOLO_LETRAS])
    nombres = models.CharField(max_length=60, validators=[SOLO_LETRAS])
    nacionalidad = models.CharField(max_length=20, validators=[SOLO_LETRAS])
    lugarnacimiento = models.CharField(max_length=60, help_text='Ej: Manta - Manabí')
    fechanacimiento = models.DateField()
    numerocedula = models.CharField(max_length=10, unique=True, validators=[SOLO_NUMEROS])
    sexo = models.CharField(max_length=1, choices=[('H','Hombre'),('M','Mujer')])
    estadocivil = models.CharField(max_length=15, choices=ESTADO_CIVIL_CHOICES)
    licenciaconducir = models.CharField(max_length=2, choices=LICENCIA_CHOICES, default='No')
    telefonoconvencional = models.CharField(max_length=15, blank=True, null=True, validators=[SOLO_NUMEROS])
    telefonofijo = models.CharField(max_length=15, blank=True, null=True, validators=[SOLO_NUMEROS])
    direcciontrabajo = models.CharField(max_length=50, blank=True, null=True)
    direcciondomiciliaria = models.CharField(max_length=50, blank=True, null=True)
    sitioweb = models.URLField(max_length=600, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    fotodeperfil = CloudinaryField('foto de perfil', blank=True, null=True)

    def clean(self):
        if self.fechanacimiento >= timezone.now().date():
            raise ValidationError({'fechanacimiento':'La fecha de nacimiento no puede ser hoy ni futura.'})

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"



class ExperienciaLaboral(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    cargodesempenado = models.CharField(max_length=300)
    nombrempresa = models.CharField(max_length=50)
    lugarempresa = models.CharField(max_length=50)
    emailempresa = models.CharField(max_length=100, blank=True, null=True)
    sitiowebempresa = models.CharField(max_length=1000, blank=True, null=True)
    nombrecontactoempresarial = models.CharField(max_length=100, blank=True, null=True)
    telefonocontactoempresarial = models.CharField(max_length=60, blank=True, null=True)
    fechainiciogestion = models.DateField()
    fechafingestion = models.DateField(blank=True, null=True)
    descripcionfunciones = models.CharField(max_length=300, blank=True, null=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutacertificado = CloudinaryField('certificado', blank=True, null=True)

    def clean(self):
        hoy = timezone.now().date()

        if self.fechainiciogestion > hoy:
            raise ValidationError({'fechainiciogestion': 'La fecha de inicio no puede ser futura.'})

        if self.fechafingestion:
            if self.fechafingestion < self.fechainiciogestion:
                raise ValidationError({'fechafingestion': 'La fecha de finalización no puede ser menor que la de inicio.'})

    def __str__(self):
        return f"{self.cargodesempenado} en {self.nombrempresa}"


class Reconocimientos(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    tiporeconocimiento = models.CharField(
        max_length=100,
        choices=[('Académico', 'Académico'), ('Público', 'Público'), ('Privado', 'Privado')]
    )
    fechareconocimiento = models.DateField()
    descripcionreconocimiento = models.CharField(max_length=300, blank=True, null=True)
    entidadpatrocinadora = models.CharField(max_length=100, blank=True, null=True)
    nombrecontactoauspicia = models.CharField(max_length=100, blank=True, null=True)
    telefonocontactoauspicia = models.CharField(max_length=60, blank=True, null=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutacertificado = CloudinaryField('reconocimiento_PDFIMG', blank=True, null=True)
    reconocimientodelacolumnadearriba = CloudinaryField('certificado_IMG', blank=True, null=True)


    def clean(self):
        if self.fechareconocimiento > timezone.now().date():
            raise ValidationError({
                'fechareconocimiento': 'La fecha del reconocimiento no puede ser futura.'
            })

    def __str__(self):
        return f"{self.tiporeconocimiento} - {self.perfil}"


class CursoRealizado(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombrecurso = models.CharField(max_length=100)
    fechainicio = models.DateField()
    fechafin = models.DateField(blank=True, null=True)
    totalhoras = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        blank=True,
        null=True
    )
    descripcioncurso = models.CharField(max_length=300, blank=True, null=True)
    entidadpatrocinadora = models.CharField(max_length=100, blank=True, null=True)
    nombrecontactoauspicia = models.CharField(max_length=100, blank=True, null=True)
    telefonocontactoauspicia = models.CharField(max_length=60, blank=True, null=True)
    emailempresapatrocinadora = models.CharField(max_length=60, blank=True, null=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutacertificado = CloudinaryField('certificado_PDF', blank=True, null=True)
    imagendelacolumnadearriba = CloudinaryField('certificado_IMG', blank=True, null=True)

    def clean(self):
        hoy = timezone.now().date()

        if self.fechainicio > hoy:
            raise ValidationError({'fechainicio': 'La fecha de inicio no puede ser futura.'})

        if self.fechafin:
            if self.fechafin > hoy:
                raise ValidationError({'fechafin': 'La fecha de finalización no puede ser futura.'})
            if self.fechafin < self.fechainicio:
                raise ValidationError({'fechafin': 'La fecha de finalización no puede ser menor que la de inicio.'})

    def __str__(self):
        return f"{self.nombrecurso} - {self.perfil}"


class ProductosAcademicos(models.Model):
    CLASIFICACION_CHOICES = [
        ('ARTICULO', 'Artículo científico'),
        ('PONENCIA', 'Ponencia'),
        ('PROYECTO', 'Proyecto de investigación'),
        ('LIBRO', 'Libro'),
        ('CAPITULO', 'Capítulo de libro'),
        ('RECURSO', 'Recurso didáctico'),
    ]

    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombrerecurso = models.CharField(max_length=100)
    clasificador = models.CharField(
        max_length=20,
        choices=CLASIFICACION_CHOICES,
        blank=True,
        null=True
    )
    descripcion = models.CharField(max_length=300, blank=True, null=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutaproductoacademico = CloudinaryField('imagen del producto académico', blank=True, null=True)

    def __str__(self):
        return f"{self.nombrerecurso} - {self.perfil}"



class ProductoLaboral(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombreproducto = models.CharField(max_length=100)
    fechaproducto = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutaproductolaboral = models.CharField(max_length=500, blank=True, null=True)

    def clean(self):
        if self.fechaproducto and self.fechaproducto > timezone.now().date():
            raise ValidationError({
                'fechaproducto': 'La fecha del producto no puede ser futura.'
            })

    def __str__(self):
        return f"{self.nombreproducto} - {self.perfil}"


class VentaGarage(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombreproducto = models.CharField(max_length=100)
    estadoproducto = models.CharField(
        max_length=40,
        choices=[('Bueno', 'Bueno'), ('Regular', 'Regular')]
    )
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    valordelbien = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        blank=True,
        null=True
    )
    fechapublicacion = models.DateField(default=timezone.localdate)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutaproducto = CloudinaryField('ruta del producto', blank=True, null=True)

    def clean(self):
        if self.fechapublicacion > timezone.localdate():
            raise ValidationError({
                'fechapublicacion': 'La fecha de publicación no puede ser futura.'
            })

    def __str__(self):
        return f"{self.nombreproducto} - {self.perfil}"
