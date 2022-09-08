from msilib.schema import Class
from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    origen=models.CharField(max_length=20)
    precio=models.IntegerField()
    descripcion= models.TextField(default="sin descripcion")

class Proveedor(models.Model):
    origen=models.CharField(max_length=20)
    proveedor= models.CharField(max_length=20)

class Sugerencia(models.Model):
    nombre=models.CharField(max_length=20)
    sugerencia=models.CharField(max_length=300)
    