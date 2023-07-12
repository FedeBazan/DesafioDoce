from django.shortcuts import render, HttpResponse
from django.template import loader
from django.urls import reverse
from .models import Usuario, Categoria, Etiqueta, Articulo

#fddsfsdf
# Create your views here.
def home(request):
    name = Usuario.objects.all()
    titulo = Articulo.objects.all()
    nombre = Categoria.objects.all()
    nombreE = Etiqueta.objects.all()
    template = loader.get_template('home/index.html')
    context = {
        "name":name,
        "titulo":titulo,
        "nombre":nombre,
        "nombreE":nombreE,
    }
    
    return HttpResponse(template.render(context, request))


 


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')


def form(request):
    return render(request, 'home/form.html')