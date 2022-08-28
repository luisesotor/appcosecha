from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def inicio (request):
    
    return render(request, "appcosecha/inicio.html")

def frutos (request):
    
    return render(request, "appcosecha/frutos.html")


def frutas(request):

    return render(request, "appcosecha/frutas.html")


def mix(request):

    return render(request, "appcosecha/mix.html")
