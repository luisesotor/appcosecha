from msilib.schema import Class
from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    origen=models.CharField(max_length=20)
    precio=models.IntegerField()
    descripcion= models.TextField(default="sin descripcion")

class Proveedor(models.Model):
    empresa=models.CharField(max_length=20)
    productos = models.TextField()

class Sugerencia(models.Model):
    nombre=models.CharField(max_length=20)
    sugerencia=models.TextField()
    