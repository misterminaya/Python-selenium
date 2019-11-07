import sys

from Pages.PageIndex import *
from Pages.FlightPage import *
from Pages.PageRegister import *
from Helpers.data import *
from Helpers.xmlReader import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class newTours(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.configuration = xmlReader()
        if self.configuration.obtener_datos('browser') == "chrome":
            self.driver = webdriver.Chrome('driver/chromedriver.exe')
        else:
            self.driver = webdriver.Chrome('driver/chromedriver.exe', options=chrome_options)
        #self.driver.get('http://newtours.demoaut.com')
        self.driver.get(self.configuration.obtener_datos('url'))
        self.page_index = PageIndex(self.driver)
        self.page_flight = FlightPage(self.driver)
        self.page_register = PageRegister(self.driver)


    def test_dropdown(self):
        my_data = test_data()
        self.page_index.click_register()
        self.page_flight.select_country_by_index(5)
        self.page_flight.select_country_by_value("11")
        self.page_flight.select_country_by_name(my_data.country)
        self.page_flight.verify_country("CONGO")
        self.page_flight.verify_not_country("ITALY")


    @unittest.skipIf(2>1,"Quiero que 1 sea mas que 2")
    def test_register(self):
        self.page_index.login('test', 'test')
        self.page_register.verify_registration_form()
        print("Complete test")

    def test_login_by_tabs(self):
        self.page_index.login_by_tab('test', 'test')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

#    if __name__ == '__main__':
#        unittest.main(
#            testRunner=xmlrunner.XMLTestRunner(output=='output'),
#            failfast=False, buffer=False, catchbreak=False)

    if __name__ == '__main__':
        #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report.html'))
        unittest.main()