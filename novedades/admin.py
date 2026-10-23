from django.contrib import admin
from .models import Noticia

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'fecha_publicacion')
    list_filter = ('tipo',)
    search_fields = ('titulo', 'resumen')