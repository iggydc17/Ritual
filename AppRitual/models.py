from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.conf import settings

class Trabajadore(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    sector = models.CharField(max_length=20)
    telefono = models.CharField(max_length=10, verbose_name="Teléfono")
    email = models.EmailField()
    fechaContratacion = models.DateField(verbose_name="Fecha Contratación")
    salario = models.IntegerField()
    foto_id = models.ImageField(upload_to='fotos_id', blank=True) # Campo no obligatorio para agilizar el proceso, ya que es una app de prueba. (La foto todavía no se visualiza)
    anotaciones = models.TextField(blank=True, verbose_name="Anotaciones (opcionales)")


    def __str__(self):
        return f'{self.nombre} {self.apellido} | {self.sector} | {self.telefono} | {self.email} | Fecha Contratación: {self.fechaContratacion} | Salario: {self.salario} '

class ReservasMesa(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fechaSolicitud = models.DateField(verbose_name="Fecha Solicitud")
    fechaReserva = models.DateTimeField(verbose_name="Fecha Reserva")
    horaReserva = models.TimeField(verbose_name="Hora Reserva")
    numeroPersonas = models.IntegerField(verbose_name="Número Personas")
    telefono = models.CharField(max_length=10, verbose_name="Teléfono")
    email = models.EmailField(blank=True, null=True, verbose_name="Email (opcional)")
    #costo = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name="Costo (opcional)")
    estado = models.BooleanField(verbose_name="Estado: (activo ✔ / inactivo ✘)")
    anotaciones = models.TextField(blank=True, verbose_name="Anotaciones (Opcional)")

    def __str__(self):
        return f'{self.nombre} {self.apellido} | Fecha Solicitud: {self.fechaSolicitud} | Fecha Reserva: {self.fechaReserva} {self.horaReserva} | Número Personas: {self.numeroPersonas} | {self.telefono} | {self.estado} | '


class Evento(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    tipoEvento = models.CharField(max_length=40, verbose_name="Tipo Evento")
    privado = models.BooleanField(verbose_name="Evento Privado (privado ✔ / semiprivado ✘)")
    fechaSolicitud = models.DateTimeField(verbose_name="Fecha Solicitud")
    fechaEvento = models.DateTimeField(verbose_name="Fecha Evento")
    horaEvento = models.TimeField(verbose_name="Hora Evento",null=True)
    numeroInvitados = models.IntegerField(verbose_name="Número Invitados (máx 115)",
        validators=[MaxValueValidator(115)])   # Se importa MaxValueValidator para establecer como tope máximo de invitados.
    telefono = models.CharField(max_length=10, verbose_name="Teléfono")
    email = models.EmailField(blank=True, null=True, verbose_name="Email (opcional)")
    duracion = models.IntegerField(verbose_name="Duración (horas)")
    costo = models.IntegerField(blank=True, verbose_name="Costo: (opcional)")
    estado = models.BooleanField(verbose_name="Estado (activo ✔ / inactivo ✘)")
    anotaciones = models.TextField(blank=True, verbose_name="Anotaciones (opcional)")

    def __str__(self):
        return f'{self.nombre} {self.apellido} | Tipo: {self.tipoEvento} | Fecha Solicitud: {self.fechaSolicitud} | Fecha Evento: {self.fechaEvento} {self.horaEvento} | Cant. Invitados: {self.numeroInvitados} | {self.telefono} | {self.estado} | Duración: {self.duracion} | Costo: ${self.costo}'


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null=True, blank=True)

    def _str_(self):
        return f'{self.user} {self.image}'


class EditPerfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    sector = models.CharField(max_length=20)
    fecha_contratacion = models.DateField(verbose_name="Fecha Contratación")
    telefono = models.CharField(max_length=10, verbose_name="Teléfono")
    redes = models.URLField(blank=True, verbose_name="Redes Sociales")
    descripcion = models.TextField(blank=True, verbose_name="Descripción (Opcional)")

    def _str_(self):
        return f'{self.user.username} ({self.sector})'

class Blog(models.Model):
    titulo = models.CharField(max_length=70)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    video = models.FileField(upload_to='blog_videos/', null=True, blank=True)
    archivo_pdf = models.FileField(upload_to='blog_files/', null=True, blank=True)

    def __str__(self):
        return f" {self.titulo} {self.autor} {self.fechaPublicacion} "



