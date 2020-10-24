from django.db import models

# Create your models here.
class services (models.Model):
    titlees = models.CharField(max_length=200, verbose_name='titulo')
    subtitlees = models.CharField(max_length=200, verbose_name='subtitulo')
    contentes = models.TextField(verbose_name='contenido')
    imagees = models.ImageField(verbose_name='imagen', upload_to='services')
    createdes = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    updatedes = models.DateTimeField(auto_now=True, verbose_name='fecha de edicion ')
    class meta:
        db_tabla ='service'
        verbose_name ='service'
        verbose_name_plural ='servicios'
        ordering = ['-created']
    def __str__(self):
        return self.titlees