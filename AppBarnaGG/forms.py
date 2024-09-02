from django import forms

class cursoFormulario(forms.Form):

    nombre = forms.CharField(max_length=20)
    camada = forms.IntegerField()
    
class contactoFormulario(forms.Form):

    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.CharField(max_length=20)
    empresa = forms.CharField(max_length=20)
    
class jugadasFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    link = forms.URLField()

class buscar(forms.Form):
    email = forms.IntegerField()