from django.urls import path

from appcosecha.models import *
from .views import *




urlpatterns = [
    
    path('mix/',mix, name='mix'),
    path('frutos/',frutos, name='frutos'),
    path('nosotros/',nosotros, name= 'nosotros'),
    path('listadeprecios/', listadeprecios, name='listasdeprecios'),
    path('inicio/',inicio , name= 'inicio'),
    
]
