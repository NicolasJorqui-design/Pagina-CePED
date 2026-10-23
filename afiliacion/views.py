from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SolicitudAfiliacionForm

def solicitar_afiliacion(request):
    if request.method == 'POST':
        form = SolicitudAfiliacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu solicitud ha sido enviada con éxito! La comisión analizará tus datos.')
            return redirect('inicio')
    else:
        form = SolicitudAfiliacionForm()

    # Asegúrate de que la ruta aquí sea 'afiliacion/solicitar.html'
    return render(request, 'afiliacion/solicitar.html', {'form': form})