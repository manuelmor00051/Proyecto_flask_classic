# Inversiones en Criptomonedas y su registro en Base de datos

Aplicación Web que controla los movimientos e inversiones en Criptomonedas y los registra en una base de datos.

# Novedades en esta versión respecto a la versión de la primera entrega.

1. La aplicación creará la base de datos cuando esta no exista. Creará el directorio de la base de datos, la propia base de datos y sus tablas y los creará solo cuando no existan.

2. Al crearse la base de datos automáticamente, se elimina un paso de la instalación en la que el usuario debía crear la base de datos manualmente.

3. También se soluciona el error de funcionamiento al estar la base de datos vacía de la entrega anterior. 

# Instrucciones de Instalación y Ejecución
1. Crear y activar el entorno virtual.

2. Instalar los softwares requeridos con pip.
```
pip install -r requirements.txt
```
3. Crear las variables de entorno, para ello duplicamos el fichero .env_template, lo renombramos como .env y dentro de este nuevo fichero cambiamos el contenido de FLASK_ENV por FLASK_ENV=development.

4. Copiar y pegar el archivo config_template.py, renombrarlo como config.py. introducir en SECRET_KEY una clave secreta para el token e introducir en API_KEY su clave personal de conexión a la api.

5.  Para la ejecución introduciremos `flask run` en el terminal.