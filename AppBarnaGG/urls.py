from AppBarnaGG import views
from django.urls import path


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),  #Le damos un nuevo argumento, indicando el nombre de la vista. para que al tocar cada boton, django sepa a donde ir.
    path('cursos/', views.cursoFormulario2, name='cursos'),
    path('contacto/', views.contactoFormulario2, name='contacto'),
    path('jugadas/', views.jugadasFormulario2, name='jugadas'),
    path('buscador/', views.buscador, name='buscador'),
    path('buscar/', views.buscar, name="buscar"),
    
]