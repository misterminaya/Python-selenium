from selenium.webdriver.support.ui import Select
import unittest

class FlightPage:
    def __init__(self,myDriver):
        self.driver = myDriver

    def select_country_by_index(self, index):
        countryDropDown = Select(self.driver.find_element_by_name("country"))
        countryDropDown.select_by_index(index)

    def select_country_by_value(self, value):
        countryDropDown = Select(self.driver.find_element_by_name("country"))
        countryDropDown.select_by_value(value)

    def select_country_bv_name(self, name):
        countryDropDown = Select(self.driver.find_element_by_name("country"))
        countryDropDown.select_by_visible_text(name)

    def verify_country(self, country):
        countryDropDown = Select(self.driver.find_element_by_name("country"))
        tc = unittest.TestCase('__init__')
        tc.assertEqual(countryDropDown.first_selected_option.text.strip(), country)

    def verify_not_country(self, country):
        countryDropDown = Select(self.driver.find_element_by_name("country"))
        tc = unittest.TestCase('__init__')
        tc.assertNotEqual(countryDropDown.first_selected_option.text.strip(), country)

    def verify_true_country(self, country):
        countryDropDown = Select(self.driver.find_element_by_name("country"))
        tc = unittest.TestCase('__init__')
        tc.assertTrue(countryDropDown.first_selected_option.text.strip() == country)

    def verify_false_country(self, country):
        countryDropDown = Select(self.driver.find_element_by_name("country"))
        tc = unittest.TestCase('__init__')
        tc.assertFalse(countryDropDown.first_selected_option.text.strip() != country)
        tc.assertFalse(countryDropDown.first_selected_option.text.strip() == country)
