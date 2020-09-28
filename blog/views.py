from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Publicacion
from .forms import PublicacionForm
from django.shortcuts import redirect

# Create your views here.
def publicacion_lista(request):
    publicaciones = Publicacion.objects.filter(
        fechapublicacion__lte=timezone.now()).order_by('fechapublicacion')
    
    return render(request, 'blog/publicacion_lista.html', {'publicaciones':publicaciones})

def publicacion_detalle(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    
    return render(request, 'blog/publicacion_detalle.html', {'publicacion': publicacion}) 

def publicacion_nueva(request):
    if request.method == "POST":
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor = request.user
            publicacion.fechapublicacion = timezone.now()
            publicacion.save()
            return redirect('publicacion_detalle', pk=publicacion.pk)
    else:
        form = PublicacionForm()
    return render(request, 'blog/publicacion_editar.html', {'form': form})

def publicacion_editar(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        form = PublicacionForm(request.POST, instance=publicacion)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor = request.user
            publicacion.fechapublicacion = timezone.now()
            publicacion.save()
            return redirect('publicacion_detalle', pk=publicacion.pk)
    else:
        form = PublicacionForm(instance=publicacion)
    return render(request, 'blog/publicacion_editar.html', {'form': form})