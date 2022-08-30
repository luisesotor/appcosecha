from django.urls import path
from .views import *




urlpatterns = [
    
    path('mix/',mix),
    path('frutos/',frutos),
    path('frutas/',frutas),
    
]
