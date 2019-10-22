
import unittest
from selenium import webdriver
from Pages.PageIndex import *
from Pages.FlightPage import *
from Pages.PageRegister import *

class newTours(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('driver/chromedriver.exe')
        self.driver.get('http://newtours.demoaut.com')
        self.page_index = PageIndex(self.driver)
        self.page_flight = FlightPage(self.driver)
        self.page_flight = FlightPage(self.driver)
        self.page_register = PageRegister(self.driver)
        time.sleep(5)

    def test_dropdown(self):
        self.page_index.click_register()
        self.page_flight.select_country_by_index(5)
        self.page_flight.select_country_by_value("11")
        self.page_flight.select_country_bv_name("CONGO")
        print("1")
        self.page_flight.verify_country("CONGO")
        print("2")
        self.page_flight.verify_not_country("ITALY")
        print("3")

    def test_register(self):
        self.page_index.login('test', 'test')
        link_registration_form = self.driver.find_element_by_link_text("registration form")
        self.assertEqual(link_registration_form.text, "registration form")
        print("Complete test")


    def tearDown(self):
        self.driver.quit()

