from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

 #Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100, verbose_name='nombre')
    createdes = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    updatedes = models.DateTimeField(auto_now=True, verbose_name='fecha de edicion ')

    class mmeta:
        db_tabla = 'categoria'
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['-created']

    def __str__(self):
        return self.name

class post ( models.Model ):
    title = models.CharField(max_length=100, verbose_name='titulo')
    content = RichTextField(verbose_name='contenido')
    published = models.DateTimeField(verbose_name='fecha de publicasion ', default=now)
    image = models.ImageField(verbose_name='imagen', upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField(category, verbose_name='categoria', related_name="get_posts")
    createdes = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    updatedes = models.DateTimeField(auto_now=True, verbose_name='fecha de edicion ')

    class Meta1:
        db_tabla = 'entrada'
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ['-created']

    def __str__(self):
        return self.title

