from django import forms

class SugerenciaFormulario(forms.Form):
    nombre= forms.CharField(max_length=20)
    sugerencia=forms.CharField(max_length=200)