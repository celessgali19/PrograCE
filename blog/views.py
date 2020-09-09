from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion

# Create your views here.
def publicacion_lista(request):
    publicaciones = Publicacion.objects.filter(
        fechapublicacion__lte=timezone.now()).order_by('fechapublicacion')
    
    return render(request, 'blog/publicacion_lista.html', {'publicaciones':publicaciones})