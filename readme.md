# Inversiones en Criptomonedas y su registro en Base de datos

Aplicación Web que controla los movimientos e inversiones en Criptomonedas y los registra en Base de datos

# Instrucciones de Instalación y Ejecución
1. Crear y activar el entorno virtual.

2. Instalar los softwares requeridos con pip.
```
pip install -r requirements.txt
```
3. Crear las variables de entorno, para ello duplicamos el fichero .env_template, lo renombramos como .env y dentro de este nuevo fichero cambiamos el contenido de FLASK_ENV por FLASK_ENV=development.

4. Copiar y pegar el archivo config_template.py, renombrarlo como config.py. Introducir en BASE_DE_DATOS el directorio donde se guardará la base de datos, introducir en SECRET_KEY una clave secreta para el token e introducir en API_KEY su clave personal de conexión a la api.

5. En el directorio elegido en el punto 4, se deberá crear una base de datos con las siguientes tablas:
```
CREATE TABLE "Movimientos" (
	"fecha"	TEXT NOT NULL,
	"hora"	TEXT NOT NULL,
	"coinsfrom"	REAL NOT NULL,
	"qf"	REAL NOT NULL,
	"coinsto"	REAL NOT NULL,
	"qt"	REAL NOT NULL,
	"pu"	REAL
)
```
```
CREATE TABLE "saldo" (
	"ETH"	REAL NOT NULL,
	"LTC"	REAL NOT NULL,
	"BNB"	REAL NOT NULL,
	"EOS"	REAL NOT NULL,
	"XLM"	REAL NOT NULL,
	"TRX"	REAL NOT NULL,
	"BTC"	REAL NOT NULL,
	"XRP"	REAL NOT NULL,
	"BCH"	REAL NOT NULL,
	"USDT"	REAL NOT NULL,
	"BSV"	REAL NOT NULL,
	"ADA"	REAL NOT NULL,
	"inversión"	REAL NOT NULL
)
```

6. Para la ejecución introduciremos `flask run` en el terminal.