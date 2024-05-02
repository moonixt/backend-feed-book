from django.db import models

# Create your models here.


class Album(models.Model):
    capa = models.ImageField( default='blank.png', upload_to='upload/images', null=False, blank=True)
    nome = models.CharField(max_length=50)
    artista = models.CharField(max_length=50)
    ano = models.DateField(auto_now=False, auto_now_add=False)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
