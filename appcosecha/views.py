from django.shortcuts import render
from django.http import HttpResponse
from appcosecha.forms import SugerenciaFormulario
from appcosecha.models import *

# Create your views here.
def inicio (request):
    
    productos=Producto.objects.all()

    return render(request, "appcosecha/inicio.html", {'productos':productos})
   
def nosotros(request):

    return render(request, "appcosecha/nosotros.html")

def listadeprecios(request):

    return render(request, "appcosecha/listadeprecios.html")

def formulariosugerencias(request):

    if request.method == 'POST':

        miformulario = SugerenciaFormulario(request.Post)

        print(miformulario)

        if miformulario.is_valid:

            informacion = miformulario.cleaned_data

            sugerencia = Sugerencia(
                nombre=informacion['nombre'], sugerencia=informacion['sugerencia'])
            sugerencia.save()
            
            return render(request, "appcosecha/inicio.html")
    else:
        miformulario = SugerenciaFormulario

    return render(request, "appcosecha/sugerencias.html", {"miformulario": miformulario})
