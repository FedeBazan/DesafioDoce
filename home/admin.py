from django.contrib import admin
from .models import Categoria, Etiqueta, Articulo, Usuario


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Etiqueta)
admin.site.register(Articulo)
admin.site.register(Usuario)