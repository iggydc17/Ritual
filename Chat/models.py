from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Conversacion(models.Model):
    # participantes = models.ManyToManyField(User, related_name='chats')
    emisor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='emisor',)
    receptor= models.ForeignKey(User, on_delete=models.CASCADE, related_name='receptor')
    def __str__(self):
        return f'{self.id}'

    def save(self):
        return self.id

class Mensaje(models.Model):
    # emisor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mensajesEnviados',)
    # receptor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mensajesRecibidos')
    conversacion = models.ForeignKey(Conversacion,on_delete=models.CASCADE)
    contenido = models.TextField()
    fechaEnvio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.id} {self.emisor} {self.fechaEnvio}'
