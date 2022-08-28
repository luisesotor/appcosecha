from django.urls import path
from .views import *



urlpatterns = [
    
    path('inicio/', inicio ),
    path('mix/',mix),
    path('frutos/',frutos),
    path('frutas/',frutas),
    
]
