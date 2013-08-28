Paso 1
=======
Descargue la ultima version de selenium-server y guardelo en la carpeta selenium-jar

Paso 2
========
Descargue los webdrivers de los navegadores con los que trabajara y guardelos en la carpeta selenium-node/drivers

Paso 3
=======
Cree el archivo local_settings.txt y escriba dentro de el la url para conectarse al hub.
Ejemplo:
http://192.168.1.2:4444/grid/register

Paso 4
======
Cree el archivo local_settings.py para definir los parametros de conexion al servidor hub y la pagina de test

Ejemplo:

IP_SERVER ="192.168.1.2"
PORT_HUB = "4444"
DIR_NAME_HUB = "/wd/hub"
PORT_WEB = "8000"
DIR_NAME_WEB="/example/"



