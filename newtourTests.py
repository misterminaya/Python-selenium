
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class newTours(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('driver/chromedriver.exe')
        self.driver.get('http://newtours.demoaut.com')
        time.sleep(5)

    def test_dropdown(self):
        self.driver.find_element_by_link_text("REGISTER").click()
        countryDropDown = Select(self.driver.find_element_by_name("country"))
        countryDropDown.select_by_index(5)
        countryDropDown.select_by_value("11")
        countryDropDown.select_by_visible_text("CONGO")
        #self.assertEquals(countryDropDown.first_selected_option.text.strip(),"CONGO")
        #self.assertNotEquals(countryDropDown.first_selected_option.text.strip(), "ITALY")
        self.assertTrue(countryDropDown.first_selected_option.text.strip() == "CONGO")
        self.assertFalse(countryDropDown.first_selected_option.text.strip() == "ARGENTINA")
        self.assertFalse(countryDropDown.first_selected_option.text.strip() != "CONGO")
        print("Test Complete")

    def test_register(self):
        user_box = self.driver.find_element_by_name('userName').send_keys('test')
        pass_box = self.driver.find_element_by_name('password').send_keys('test')
        submit_button = self.driver.find_element_by_name('login').click()
        link_registration_form = self.driver.find_element_by_link_text("registration form")
        #assert link_registration_form.text == "registration form"
        self.assertEquals(link_registration_form.text,"registration form")
        print("Complete test")


    def tearDown(self):
        self.driver.quit()