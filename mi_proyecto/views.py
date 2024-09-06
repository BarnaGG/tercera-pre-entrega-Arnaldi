from django.http import HttpResponse
from django.template import Template, Context # Agregamos al encabezado del archivo el import de Template y de Context
from django.template import loader
from AppBarnaGG.models import Curso

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def otra_vista(request):
    return HttpResponse("<h1>¡Esto es un título!</h1><p>Y este es un párrafo.</p>")


def probando_template(request):

    nom = "Bruno"
    ap = "Arnaldi"
    ListaDeNotas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    diccionario = {"Nombre": nom, "Apellido": ap, "Notas": ListaDeNotas}

    plantilla = loader.get_template('template1.html')

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

def agregar_curso(request, nom, cam):
    curso = Curso(nombre=nom, camada=cam)
    curso.save()
    
    return HttpResponse("Curso agregado")