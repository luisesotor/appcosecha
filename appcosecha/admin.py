from atexit import register
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Sugerencia)