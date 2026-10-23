from django.shortcuts import render
from novedades.models import Noticia

def inicio(request):
    # Obtenemos las últimas 3 noticias/eventos publicados
    ultimas_noticias = Noticia.objects.all()[:3]
    context = {
        'ultimas_noticias': ultimas_noticias
    }
    return render(request, 'core/inicio.html', context)

def quienes_somos(request):
    return render(request, 'core/quienes_somos.html')

def preguntas_frecuentes(request):
    return render(request, 'core/preguntas_frecuentes.html')