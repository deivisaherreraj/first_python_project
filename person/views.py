from django.shortcuts import render
# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
# Habilitamos los formularios en Django
from django import forms
# Instanciamos el modelo 'Person' para poder usarlo en nuestras Vistas CRUD
from .models import STATUS_STRESS_LEVEL, Person

# Create your views here.
class PersonList(ListView): 
    model = Person # Llamamos a la clase 'Person' que se encuentra en nuestro archivo 'models.py'

class PersonView(DetailView): 
    model = Person # Llamamos a la clase 'Person' que se encuentra en nuestro archivo 'models.py'
    
class PersonCreate(SuccessMessageMixin, CreateView): 
    model = Person # Llamamos a la clase 'Person' que se encuentra en nuestro archivo 'models.py'
    form = Person # Definimos nuestro formulario con el nombre de la clase o modelo 'Person'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Person' de nuestra Base de Datos 
    success_message = 'Persona creada correctamente !' # Mostramos este mensaje luego de crear una persona
 
    # Redireccionamos a la página principal luego de crear un registro o persona
    def get_success_url(self):        
        return reverse('read') # Redireccionamos a la vista principal 'leer'

class PersonUpdate(SuccessMessageMixin, UpdateView): 
    model = Person # Llamamos a la clase 'Person' que se encuentra en nuestro archivo 'models.py' 
    form = Person # Definimos nuestro formulario con el nombre de la clase o modelo 'Person' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Person' de nuestra Base de Datos 
    success_message = 'Persona actualizado correctamente !' # Mostramos este mensaje luego de editar una persona
 
    # Redireccionamos a la página principal luego de actualizar un registro o persona
    def get_success_url(self):               
        return reverse('read') # Redireccionamos a la vista principal 'leer'

class PersonDelete(SuccessMessageMixin, DeleteView): 
    model = Person 
    form = Person
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o persona
    def get_success_url(self): 
        success_message = 'Persona eliminado correctamente !' # Mostramos este mensaje luego de editar una persona 
        messages.success(self.request, (success_message))       
        return reverse('read') # Redireccionamos a la vista principal 'leer'