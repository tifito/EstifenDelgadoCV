from django.db import models

# Tabla principal: Perfil
class DatosPersonales(models.Model):
    descripcionperfil = models.CharField(max_length=50)
    perfilactivo = models.BooleanField(default=True)
    apellidos = models.CharField(max_length=60)
    nombres = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=20)
    lugarnacimiento = models.CharField(max_length=60)
    fechanacimiento = models.DateField()
    numerocedula = models.CharField(max_length=10, unique=True)
    sexo = models.CharField(max_length=1, choices=[('H', 'Hombre'), ('M', 'Mujer')])
    estadocivil = models.CharField(max_length=50)
    licenciaconducir = models.CharField(max_length=6, blank=True, null=True)
    telefonoconvencional = models.CharField(max_length=15, blank=True, null=True)
    telefonofijo = models.CharField(max_length=15, blank=True, null=True)
    direcciontrabajo = models.CharField(max_length=50, blank=True, null=True)
    direcciondomiciliaria = models.CharField(max_length=50, blank=True, null=True)
    sitioweb = models.CharField(max_length=60, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    fotodeperfil=models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


# Experiencia Laboral
class ExperienciaLaboral(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    cargodesempenado = models.CharField(max_length=100)
    nombrempresa = models.CharField(max_length=50)
    lugarempresa = models.CharField(max_length=50)
    emailempresa = models.CharField(max_length=100, blank=True, null=True)
    sitiowebempresa = models.CharField(max_length=100, blank=True, null=True)
    nombrecontactoempresarial = models.CharField(max_length=100, blank=True, null=True)
    telefonocontactoempresarial = models.CharField(max_length=60, blank=True, null=True)
    fechainiciogestion = models.DateField()
    fechafingestion = models.DateField(blank=True, null=True)
    descripcionfunciones = models.CharField(max_length=100, blank=True, null=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutacertificado = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.cargodesempenado} en {self.nombrempresa}"


# Reconocimientos
class Reconocimientos(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    tiporeconocimiento = models.CharField(
        max_length=100,
        choices=[('Académico', 'Académico'), ('Público', 'Público'), ('Privado', 'Privado')]
    )
    fechareconocimiento = models.DateField()
    descripcionreconocimiento = models.CharField(max_length=100, blank=True, null=True)
    entidadpatrocinadora = models.CharField(max_length=100, blank=True, null=True)
    nombrecontactoauspicia = models.CharField(max_length=100, blank=True, null=True)
    telefonocontactoauspicia = models.CharField(max_length=60, blank=True, null=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutacertificado = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.tiporeconocimiento} - {self.perfil}"


# Cursos Realizados
class CursoRealizado(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombrecurso = models.CharField(max_length=100)
    fechainicio = models.DateField()
    fechafin = models.DateField(blank=True, null=True)
    totalhoras = models.IntegerField(blank=True, null=True)
    descripcioncurso = models.CharField(max_length=100, blank=True, null=True)
    entidadpatrocinadora = models.CharField(max_length=100, blank=True, null=True)
    nombrecontactoauspicia = models.CharField(max_length=100, blank=True, null=True)
    telefonocontactoauspicia = models.CharField(max_length=60, blank=True, null=True)
    emailempresapatrocinadora = models.CharField(max_length=60, blank=True, null=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutacertificado = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.nombrecurso} - {self.perfil}"


# Productos Académicos
class ProductosAcademicos(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombrerecurso = models.CharField(max_length=100)
    clasificador = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutaproductoacademico=models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
        return f"{self.nombrerecurso} - {self.perfil}"


# Productos Laborales
class ProductoLaboral(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombreproducto = models.CharField(max_length=100)
    fechaproducto = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutaproductolaboral = models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
        return f"{self.nombreproducto} - {self.perfil}"


# Venta Garage
class VentaGarage(models.Model):
    perfil = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE)
    nombreproducto = models.CharField(max_length=100)
    estadoproducto = models.CharField(max_length=40, choices=[('Bueno', 'Bueno'), ('Regular', 'Regular')])
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    valordelbien = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutaproducto = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.nombreproducto} - {self.perfil}"
