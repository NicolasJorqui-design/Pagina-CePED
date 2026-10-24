# CePED - Asociación Civil de Centros Privados de Educación a Distancia de Salta

Bienvenido al repositorio oficial del sitio web institucional de CePED (Salta, Argentina). Este proyecto está desarrollado utilizando Django y Bootstrap 5, implementando una identidad visual propia en tonos blanco y dorado.

# 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado en tu sistema:

Python 3.10+: Descargar Python

Git (opcional, para gestión de versiones)

Visual Studio Code (recomendado como editor de código)

# 🛠️ Estructura del Proyecto

El proyecto está organizado en las siguientes aplicaciones Django:

projecto_ceped/
├── core/                   # App principal (Inicio, Quiénes Somos, Preguntas Frecuentes, Base HTML y CSS)
│   ├── static/css/estilo.css
│   └── templates/core/
├── novedades/              # App para gestión de Noticias y Eventos
│   └── templates/novedades/
├── afiliacion/             # App para solicitudes de adhesión e instituciones
│   └── templates/afiliacion/
├── projecto_ceped/         # Configuración global del proyecto (settings.py, urls.py)
├── static/                 # Carpeta para recolectar estáticos globales
├── manage.py               # Comando principal de Django
└── README.md


# 🚀 Guía de Instalación y Puesta en Marcha

Sigue estos pasos detallados para configurar y ejecutar la aplicación en tu entorno local:

1. Clonar o Descomprimir el Proyecto

Abre la terminal o línea de comandos y navega hasta la carpeta del proyecto:

cd projecto_ceped


2. Crear el Entorno Virtual

Un entorno virtual permite aislar las dependencias del proyecto. Ejecuta:

En Windows:

python -m venv venv_ceped


En macOS / Linux:

python3 -m venv venv_ceped


3. Activar el Entorno Virtual

En Windows (PowerShell):

.\venv_ceped\Scripts\activate


En Windows (Command Prompt - CMD):

venv_ceped\Scripts\activate.bat


En macOS / Linux:

source venv_ceped/bin/activate


(Sabrás que está activo porque aparecerá (venv_ceped) al inicio de tu terminal).

4. Instalar Dependencias

Instala los paquetes necesarios registrados para el proyecto (Django y Pillow para el procesamiento de imágenes):

python -m pip install --upgrade pip
python -m pip install django Pillow


5. Aplicar Migraciones

Prepara la base de datos local SQLite creando las tablas necesarias:

python manage.py makemigrations
python manage.py migrate


6. Crear un Superusuario (Opcional - Panel de Administración)

Para poder cargar noticias, revisar afiliaciones e interactuar desde el panel administrativo de Django:

python manage.py createsuperuser


(Sigue las instrucciones en pantalla para ingresar usuario, correo y contraseña).

7. Ejecutar el Servidor de Desarrollo

Inicia el servidor local de Django:

python manage.py runserver


Abre tu navegador e ingresa a: http://127.0.0.1:8000/

# 🎨 Características e Identidad Visual

Paleta de Colores: Blanco institucional, Azul marino y Acentos en Dorado (#C5A059).

Framework CSS: Bootstrap 5 + Iconos de Bootstrap (bootstrap-icons).

Seguridad Integrada: Protección contra ataques CSRF en todos los formularios mediante la etiqueta {% csrf_token %}.

Formularios Dinámicos: Gestión de afiliaciones y listados dinámicos de noticias.

# 👥 Colaboración y Repositorio

Al compartir el proyecto en equipo o subir cambios al repositorio:

NO incluir la carpeta venv_ceped/ ni las carpetas __pycache__/.

Asegurarse de que cada colaborador cree su propio entorno virtual localmente siguiendo los pasos descritos en este documento.