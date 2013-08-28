mkdir selenium-jar
wget http://selenium.googlecode.com/files/selenium-server-standalone-2.35.0.jar
mv selenium-server-standalone-2.35.0.jar selenium-jar/selenium-server.jar

mkdir selenium-node/drivers

wget https://chromedriver.googlecode.com/files/chromedriver_win32_2.2.zip
unzip chromedriver_win32_2.2.zip
mv chromedriver.exe selenium-node/drivers/
rm chromedriver_win32_2.2.zip

wget https://selenium.googlecode.com/files/IEDriverServer_Win32_2.35.3.zip
unzip IEDriverServer_Win32_2.35.3.zip
mv IEDriverServer.exe selenium-node/drivers/
rm IEDriverServer_Win32_2.35.3.zip