from django.shortcuts import render
from django.http import HttpResponse
from appcosecha.forms import *
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

        miformulario = SugerenciaFormulario(request.POST)

        print(miformulario)

        if miformulario.is_valid:

            informacion = miformulario.cleaned_data

            sugerencia = Sugerencia(
                nombre=informacion['nombre'], sugerencia=informacion['sugerencia'])
            sugerencia.save()
            
            return render(request, "appcosecha/inicio.html")
    else:
        miformulario = SugerenciaFormulario()

    return render(request, "appcosecha/sugerencias.html", {"miformulario": miformulario})


def crearproveedor(request):

    if request.method == 'POST':

        formularioproveedor = CrearProveedor (request.POST)

        print(formularioproveedor)

        if formularioproveedor.is_valid:

            informacion = formularioproveedor.cleaned_data

            proveedor = Proveedor(
                empresa=informacion['nombre'], producto=informacion['producto'])
            proveedor.save()

            return render(request, "appcosecha/inicio.html")
    else:
        formularioproveedor = CrearProveedor()

    return render(request, "appcosecha/crearproveedor.html", {"formularioproveedor": formularioproveedor})


def crearproducto(request):

    if request.method == 'POST':

        formularioproducto = CrearProducto(request.POST)

        print(formularioproducto)

        if formularioproducto.is_valid:

            informacion = formularioproducto.cleaned_data

            producto = Producto(
                nombre=informacion['nombre'], origen=informacion['origen'], precio=informacion['precio'], descripcion=informacion['descripcion'])
            producto.save()

            return render(request, "appcosecha/inicio.html")
    else:
        formularioproducto = CrearProducto()

    return render(request, "appcosecha/crearproducto.html", {"formularioproducto": formularioproducto})

def busqueda(request):
    return render(request, "appcosecha/busqueda.html")

def buscar(request):
    respuesta= f"Estoy buscando el producto: {request.GET['producto']}"
    return HttpResponse(respuesta)
