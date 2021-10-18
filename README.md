# kimble
kimble es un sistema para administrar la fronteca de tu sitio web

## Instalar dependencias
>- pip install -r requirements.txt

## Creación de la base de datos
>- setenv.py
>- flask db init
>- flask db migrate -m "Initial migration"
>- flask db upgrade 

## Instalación de componentes básicos
>- flask shell
>- from app.models import Setup
>- setup = Setup()
>- setup.install()
>- exit()

## Iniciar el sistema 
> Modo desarrollador
>- start.bat