from django.db import models

# Create your models here.
class mix(models.Model):
    nombre=models.CharField(max_length=50)
    ingredientes=models.CharField(max_length=200)
    precio=models.IntegerField()

class frutos(models.Model):
    nombre=models.CharField(max_length=50)
    origen=models.CharField(max_length=20)
    precio=models.IntegerField()

class frutas(models.Model):
    nombre = models.CharField(max_length=50)
    origen = models.CharField(max_length=20)
    precio = models.IntegerField()

