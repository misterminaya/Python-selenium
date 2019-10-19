from selenium import webdriver
import  unittest

class PageRegister():
    def __init__(self, myDriver):
        self.driver = myDriver


    def verify_registration_form(self):
        link_registration_form = self.driver.find_element_by_link_text("")
        tc = unittest.TestCase('__init__')
        tc.self.assertEqual(link_registration_form, "registration form")
        print("Exit code ")