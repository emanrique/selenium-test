
Descripción
=============

Este proyecto nos brinda un setup básico de test de selenium en python, utilizando el modelo hub -node.

Notas
========
El hub fue testeado en Mac y el node en Windows


Inicio Rápido
=============


Paso 1
========
Ejecute el bash get_resources.sh, este archivo descarga server-selenium y los webdrivers


Paso 2
=======
Ejecute en terminal el comando

java -jar selenium-jar/selenium-server.jar

Paso 3
=======
Cree el archivo selenium-server/local_settings.py para definir los parametros de conexion al servidor hub y la pagina de test

Ejemplo:
IP_SERVER ="192.168.1.2"
PORT_HUB = "4444"
DIR_NAME_HUB = "/wd/hub"
PORT_WEB = "8000"
DIR_NAME_WEB="/example/"



Paso 4
=======
Copie la carpeta selenium-node a la direccion de su preferencia en windows

Paso 5
=======
Cree el archivo selenium-node/local_settings.txt y escriba dentro de él la url para conectarse al hub.

Ejemplo:
http://192.168.1.2:4444/grid/register


Paso 6
=======
Ejecute el batch exec.bat

Paso 7
=======
Ejecute por terminal el comando

python selenium-server/main.py

Y listo =)




