# Django CRUD Person/User Ejemplo

Este proyecto consta para la implementación de operaciones CRUD en una sola tabla Person/User utilizando el marco web de Django.

Esta versión utiliza la versión Python 3.10.7.
Esta versión utiliza la versión Django 3.2.14.

## Instalación y Funcionamiento

Resumen:

    # Clonar el proyecto
    git clone git@github.com:deivisaherreraj/first_python_project.git
    
    cd first_python_project

    # Crear entorno virtual de Python 3
    python -m venv entorno-virtual
    . entorno-virtual\Scripts\activate

    # Instalar los paquetes necesarios (Django 3.2.14)
    pip install --upgrade pip
    pip install -r requirements.txt
    
    # Crear tablas de base de datos para el proyecto, proyecto configurado para usar SQLite DB
    python manage.py makemigrations
    python manage.py makemigrations polls
    python manage.py migrate
    python manage.py collectstatic

    # Ejecutar el servidor de desarrollo
    python manage.py runserver