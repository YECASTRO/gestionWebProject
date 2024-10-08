

### 1. Introducción



# Proyecto GestionWeb

Este proyecto es una aplicación de lista de tareas desarrollada con Python y Django. Permite a los usuarios gestionar sus tareas diarias de manera eficiente.


### 2. Arquitectura Cliente-Servidor


## Arquitectura Cliente-Servidor

Este proyecto sigue una arquitectura cliente-servidor. En esta arquitectura:

- **Cliente**: El cliente es la interfaz de usuario que interactúa con el usuario final. En este proyecto, el cliente es el navegador web que envía solicitudes HTTP al servidor y muestra las respuestas.
- **Servidor**: El servidor es la aplicación Django que maneja las solicitudes del cliente, procesa la lógica de negocio y devuelve las respuestas adecuadas.

### Diagrama de Arquitectura

[Cliente (Navegador Web)] <----> [Servidor (Django)]

### 3. Estructura de Archivos



## Estructura de Archivos

- `manage.py`: Script de utilidad para interactuar con el proyecto Django.
- `gestionWebProject/`: Directorio principal de la aplicación.
  - `settings.py`: Configuración del proyecto Django.
  - `urls.py`: Definición de las rutas URL del proyecto.
  - `wsgi.py`: Configuración para el servidor WSGI.
- `tasks/`: Directorio de la aplicación de lista de tareas.
  - `models.py`: Definición de los modelos de datos.
  - `views.py`: Lógica de las vistas que manejan las solicitudes del cliente.
  - `urls.py`: Rutas URL específicas de la aplicación.
  - `templates/`: Plantillas HTML para las vistas.
  - `static/`: Archivos estáticos como CSS y JavaScript.

### 4. Funcionalidades



## Funcionalidades

- **Crear Tareas**: Los usuarios pueden crear nuevas tareas.
- **Listar Tareas**: Los usuarios pueden ver una lista de todas las tareas.
- **Actualizar Tareas**: Los usuarios pueden editar las tareas existentes.
- **Eliminar Tareas**: Los usuarios pueden eliminar tareas que ya no son necesarias.

### 5. Instalación y Ejecución

## Instalación y Ejecución

1. Clona el repositorio:
   ```bash
   git clone https://github.com/YECASTRO/gestionWebProject.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd tu_repositorio
   ```
3. Crea un entorno virtual e instala las dependencias:
   ```bash
   python -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```
4. Realiza las migraciones y ejecuta el servidor:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
5. Abre tu navegador y visita `http://127.0.0.1:8000` para ver la aplicación en funcionamiento.

### Video demostrativo 

[Ver Video de Gestión de Tareas](https://drive.google.com/file/d/1gpKiqWeQP07nt4bhDvS1E62LobqTl75T/view?usp=sharing)

