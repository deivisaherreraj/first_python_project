"""first_python_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from person.views import PersonCreate, PersonDelete, PersonList, PersonUpdate, PersonView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # La ruta 'leer' en donde listamos todos los registros o person de la Base de Datos
    path('person/', PersonList.as_view(template_name = "person/index.html"), name='read'), 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro 
    path('person/view/<uuid:pk>', PersonView.as_view(template_name = "person/view.html"), name='view'), 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro  
    path('person/create', PersonCreate.as_view(template_name = "person/create.html"), name='create'), 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos 
    path('person/update/<uuid:pk>', PersonUpdate.as_view(template_name = "person/update.html"), name='update'),  
    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos 
    path('person/delete/<uuid:pk>', PersonDelete.as_view(), name='delete'),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
