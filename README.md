# RegisterFlaskApp

Este es un proyecto de aprendizaje que utiliza python flask, base de datos no relacional Mongo DB 

## Instalación

Instrucciones para instalar y configurar el proyecto en una máquina local.

```bash
# Clonar el repositorio
git clone https://github.com/tu_usuario/tu_proyecto.git

# Navegar al directorio del proyecto
cd LoginFlaskApp

# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows
venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate

# Instalar las dependencias
pip install -r requirements.txt

```
## Archivo .env para variables de entorno
Es necesario crear en la raiz del proyecto un archivo .env en este se deben incluir las siguientes variables de entorno:
 - STRING_CONNECTION : Cadena de conexión de la base de datos
 - DATABASE_NAME : Nombre de la base de datos
 - EMAIL_USER : Correo del usuario del correo electrónico
 - EMAIL_PASSWORD : Contraseña de aplicaciones del correo electrónico

## Ejecución 
Para correr el código solo resta colocar en consola: 
```bash
python main.py
```
