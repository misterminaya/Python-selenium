from selenium.webdriver.support.ui import Select
import unittest

class FlightPage:
    def __init__(self,myDriver):
        self.driver = myDriver
        self.countryDropDown = Select(self.driver.find_element_by_name("country"))

    def select_country_by_index(self, index):
        self.countryDropDown.select_by_index(index)

    def select_country_by_value(self, value):
        self.countryDropDown.select_by_value(value)

    def select_country_bv_name(self, name):
        self.countryDropDown.select_by_visible_text(name)

    def verify_country(self, country):
        tc = unittest.TestCase('__init__')
        tc.assertEqual(self.countryDropDown.first_selected_option.text.strip(), country)

    def verify_not_country(self, country):
        tc = unittest.TestCase('__init__')
        tc.assertNotEqual(self.countryDropDown.first_selected_option.text.strip(), country)

    def verify_true_country(self, country):
        tc = unittest.TestCase('__init__')
        tc.assertTrue(self.countryDropDown.first_selected_option.text.strip() == country)

    def verify_false_country(self, country):
        tc = unittest.TestCase('__init__')
        tc.assertFalse(self.countryDropDown.first_selected_option.text.strip() != country)
        tc.assertFalse(self.countryDropDown.first_selected_option.text.strip() == country)
