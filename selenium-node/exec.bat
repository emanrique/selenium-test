@echo off
echo Iniciando selenium server
set path=%CD%/drivers;%path%
set hub=http://localhost:4444/grid/register
FOR /F %%i IN (local_settings.txt) DO set hub=%%i
java -jar selenium-server.jar -role node -hub %hub%
pause