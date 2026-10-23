from django.db import models

class Noticia(models.Model):
    TIPO_CHOICES = [
        ('NOTICIA', 'Noticia'),
        ('EVENTO', 'Evento / Webinar / Congreso'),
    ]

    titulo = models.CharField(max_length=200, verbose_name="Título")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='NOTICIA')
    resumen = models.CharField(max_length=300, verbose_name="Resumen corto")
    contenido = models.TextField(verbose_name="Contenido completo")
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True, verbose_name="Imagen destacada")
    fecha_publicacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de publicación")

    class Meta:
        verbose_name = "Noticia o Evento"
        verbose_name_plural = "Noticias y Eventos"
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return self.titulo