from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('afiliacion/', include('afiliacion.urls')),  # Enlazamos la app afiliacion
    path('novedades/', include('novedades.urls')), # Enlazamos la app novedades
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
