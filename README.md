# desafio_guiado_Aplicacion_web_Python

## Descripción del Desafío

Un cliente ha solicitado el desarrollo de una aplicación web que contenga tres vistas principales: Home, About y Contact. La solución propuesta consiste en proporcionar un ejemplo utilizando Django. Para los contenidos de las vistas, se pueden utilizar textos de prueba generados con Lorem Ipsum. Se sugiere implementar un mini formulario de contacto con HTML en la vista de Contacto.


## Descripción de la Solución

### Creación de las Vistas

Para cumplir con los requisitos del cliente, debes crear las siguientes vistas:

1. **Vista Home**: Esta vista debería mostrar la página principal de la aplicación.
2. **Vista About**: Aquí deberías mostrar información sobre la aplicación o la empresa.
3. **Vista Contact**: En esta vista, implementa un mini formulario de contacto utilizando HTML.

Recuerda seguir las prácticas recomendadas de Django y asegurarte de que las vistas estén correctamente enlazadas a las URL correspondientes.

### Tips y Recomendaciones

- Para configurar las URLs, puedes seguir el siguiente formato:

```python
from holaMundo.views import home, about, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
    path('contact/', contact)
]
```
### Archivos Principales del Proyecto "desafio"

1. **manage.py**: Punto de entrada para administrar el proyecto Django.
2. **settings.py**: Configuración principal del proyecto.
3. **urls.py**: Define las URL del proyecto.
4. **wsgi.py**: Implementa la interfaz WSGI.

### Archivos Principales de la Aplicación "holaMundo"

1. **views.py**: Funciones de vista de la aplicación.
2. **models.py**: Define los modelos de datos.
3. **urls.py**: Define las URL específicas de la aplicación.
4. **templates/**: Contiene archivos HTML de las plantillas.

### Pasos para Crear el Proyecto desde Cero

1. **Crear Carpeta del Proyecto**:

mkdir desafio
cd desafio

2. **Crear y Activar el Entorno Virtual**:

python -m venv env
source env/Scripts/activate

3. **Instalar Django**:

pip install django==4.2

4. **Crear/Iniciar el Proyecto**:

django-admin startproject desafio .

5. **Aplicar Migraciones Pendientes**:

python manage.py migrate

6. **Crear Administrador**:

python manage.py createsuperuser

7. **Crear/Iniciar la Aplicación**:

python manage.py startapp holaMundo

8. **Iniciar el Servidor**:

**Nota**: Para crear el archivo `requirements.txt`, usa `pip freeze > requirements.txt`. Para instalar dependencias, usa `pip install -r requirements.txt`.


