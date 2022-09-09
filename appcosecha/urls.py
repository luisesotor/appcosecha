from django.urls import path

from appcosecha.models import *
from .views import *

urlpatterns = [  
    path('nosotros/',nosotros, name= 'nosotros'),
    path('listadeprecios/', listadeprecios, name='listasdeprecios'),
    path('inicio/',inicio , name= 'inicio'),
    path('sugerencias/', inicio, name='sugerencias'),
    
]
