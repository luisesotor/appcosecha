from django import forms
from appcosecha.models import *

class SugerenciaFormulario(forms.ModelForm):
    class Meta:
        model=Sugerencia
        fields='__all__'

class CrearProducto(forms.ModelForm):
    class Meta:
        model=Producto
        fields='__all__'

class CrearProveedor(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields='__all__'