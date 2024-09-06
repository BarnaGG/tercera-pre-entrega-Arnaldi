from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
from AppBarnaGG.models import Curso, contact, Jugadas
from AppBarnaGG.forms import cursoFormulario, contactoFormulario, jugadasFormulario

# Create your views here.

def inicio(req):
    return render(req, 'AppBarnaGG/inicio.html')

def cursos(req):
    return render(req, 'AppBarnaGG/cursos.html')

def contacto(req):
    return render(req, 'AppBarnaGG/contacto.html')

def jugadas(req):
    return render(req, 'AppBarnaGG/jugadas.html')

def cursoFormulario2(req):
    
    if req.method == "POST": 
        miFormulario = cursoFormulario(req.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["nombre"], camada=informacion["camada"]) 
            curso.save()
            return render(req, "AppBarnaGG/inicio.html")
    else:
        miFormulario = cursoFormulario()

    return render(req, "AppBarnaGG/cursos.html", {"miFormulario": miFormulario})

def contactoFormulario2(req):
    
    if req.method == "POST": 
        contactFormulario = contactoFormulario(req.POST)
        print(contactFormulario)

        if contactFormulario.is_valid():
            informacion = contactFormulario.cleaned_data
            contacts = contact(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], empresa=informacion["empresa"]) 
            contacts.save()
            return render(req, "AppBarnaGG/inicio.html")
    else:
        contactFormulario = contactoFormulario()

    return render(req, "AppBarnaGG/contacto.html", {"contactFormulario": contactFormulario})

def jugadasFormulario2(req):
    
    if req.method == "POST": 
        playsFormulario = jugadasFormulario(req.POST)
        print(playsFormulario)

        if playsFormulario.is_valid():
            informacion = playsFormulario.cleaned_data
            play = Jugadas(nombre=informacion["nombre"], apellido=informacion["apellido"], link=informacion["link"]) 
            play.save()
            return render(req, "AppBarnaGG/inicio.html")
    else:
        playsFormulario = jugadasFormulario()

    return render(req, "AppBarnaGG/jugadas.html", {"playsFormulario": playsFormulario})

def buscador(req):
    return render(req, "AppBarnaGG/buscador.html")

def buscar(req):
    
    if req.GET["camada"]:
        
        camada=req.GET['camada']
        lista_de_cursos=Curso.objects.filter(camada__icontains=camada)
        return render(req, "AppBarnaGG/resultadosBusqueda.html", {"lista_de_cursos":lista_de_cursos, "camada":camada})
    
    else:
        
        respuesta="No enviaste datos"
        
    return HttpResponse(respuesta)