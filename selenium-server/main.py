import time
import settings

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains




global_settings = dict((setting.lower(), getattr(settings, setting))
                       for setting in dir(settings) if setting.isupper())


class Application():

    def test_index(self):

        driver = webdriver.Remote(self.hub, DesiredCapabilities.CHROME)
        driver.get(self.web+"example/index.html")
        element = driver.find_element_by_id("footer")
        driver.execute_script('$("html, body").animate({ scrollTop: $(document).height() }, 10000);')
        driver.quit()


    def __init__(self,settings):

        self.settings = settings
        self.hub = "http://"+str(self.settings.get('ip_server'))+":"+str(self.settings.get('port_hub'))+str(self.settings.get('dir_name_hub'))
        self.web = "http://"+str(self.settings.get('ip_server'))+":"+str(self.settings.get('port_web'))+str(self.settings.get('dir_name_web'))
        self.test_index()


if __name__ == '__main__':
    application = Application(global_settings)
