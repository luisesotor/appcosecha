from django.urls import path

from appcosecha.models import *
from .views import *

urlpatterns = [  
    path('nosotros/',nosotros, name= 'nosotros'),
    path('listadeprecios/', listadeprecios, name='listasdeprecios'),
    path('inicio/',inicio , name= 'inicio'),
    path('sugerencias/',formulariosugerencias, name='sugerencias'),
    path('crearproducto/', crearproducto, name='crearproducto'),
    path('crearproveedor/', crearproveedor, name='crearproveedor'),
    path('busqueda',busqueda, name='busqueda'),
    path('buscar/', buscar)
    
]
