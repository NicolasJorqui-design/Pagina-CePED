from django.contrib import admin
from .models import SolicitudAfiliacion

@admin.register(SolicitudAfiliacion)
class SolicitudAfiliacionAdmin(admin.ModelAdmin):
    list_display = ('institucion', 'responsable_contacto', 'email', 'provincia', 'fecha_solicitud', 'procesado')
    list_filter = ('procesado', 'motivo', 'provincia')
    search_fields = ('institucion', 'responsable_contacto', 'email')