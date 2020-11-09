from django.db import models
from django.utils import timezone


class Publicacion(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    fechacreacion= models.DateTimeField('Creado',
            default=timezone.now)
    fechapublicacion = models.DateTimeField(
            blank=True, null=True)

    def publicar(self):
        self.fechapublicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo