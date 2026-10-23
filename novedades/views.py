from django.shortcuts import render, get_object_or_404
from .models import Noticia

def lista_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'novedades/lista_noticias.html', {'noticias': noticias})

def detalle_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    return render(request, 'novedades/detalle_noticia.html', {'noticia': noticia})