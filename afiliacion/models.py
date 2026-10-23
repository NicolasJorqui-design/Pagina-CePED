from django.db import models

class SolicitudAfiliacion(models.Model):
    MOTIVOS_CHOICES = [
        ('ASOCIAR', 'Quiero asociar a mi institución'),
        ('CONSULTA', 'Consulta general'),
    ]

    institucion = models.CharField(max_length=200, verbose_name="Institución")
    entidad_propietaria = models.CharField(max_length=200, verbose_name="Entidad Propietaria", blank=True, null=True)
    provincia = models.CharField(max_length=100, verbose_name="Provincia", default="Salta")
    localidad = models.CharField(max_length=100, verbose_name="Localidad")
    email = models.EmailField(verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=50, verbose_name="Teléfono")
    responsable_contacto = models.CharField(max_length=200, verbose_name="Responsable de contacto y cargo")
    motivo = models.CharField(max_length=20, choices=MOTIVOS_CHOICES, default='ASOCIAR', verbose_name="Motivo de la consulta")
    mensaje = models.TextField(verbose_name="Consulta / Mensaje", blank=True, null=True)
    fecha_solicitud = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Envío")
    procesado = models.BooleanField(default=False, verbose_name="Atendido / Procesado")

    class Meta:
        verbose_name = "Solicitud de Afiliación"
        verbose_name_plural = "Solicitudes de Afiliación"
        ordering = ['-fecha_solicitud']

    def __str__(self):
        return f"{self.institucion} - {self.responsable_contacto}"