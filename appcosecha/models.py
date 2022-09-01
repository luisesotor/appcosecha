from django.db import models

# Create your models here.
class Mix(models.Model):
    nombre=models.CharField(max_length=50)
    ingredientes=models.CharField(max_length=200)
    precio=models.IntegerField()

class Frutos(models.Model):
    nombre=models.CharField(max_length=50)
    origen=models.CharField(max_length=20)
    precio=models.IntegerField()

class Frutas(models.Model):
    nombre = models.CharField(max_length=50)
    origen = models.CharField(max_length=20)
    precio = models.IntegerField()

class Nosotros(models.Model):
    nosotros=models.CharField(max_length=300)

class Listadeprecios(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.IntegerField()
