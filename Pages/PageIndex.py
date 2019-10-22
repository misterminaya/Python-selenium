import time
from selenium.webdriver.common.by import By


class PageIndex:
    def __init__(self, myDriver):
        self.driver = myDriver
        #self.user_box = self.driver.find_element_by_name('userName')
        #self.pass_box = self.driver.find_element_by_name('password')
        #self.register_link = self.driver.find_element_by_link_text("REGISTER")
        #self.submit_button = self.driver.find_element_by_name('login')
        self.user_box = (By.NAME, 'userName')
        self.pass_box = (By.NAME, 'password')
        self.register_link = (By.LINK_TEXT, 'register')
        self.submit_button = (By.NAME, 'login')

    def click_register(self):
        #self.register_link.click()
        self.driver.find_element(*self.register_link)

    def login(self, user_name, password):
        #self.user_box.send_keys(user_name)
        #self.pass_box.send_keys(password)
        #self.submit_button.click()
        self.driver.find_element(*self.user_box).send_keys(user_name)
        self.driver.find_element(*self.pass_box).send_keys(password)
        self.driver.find_element(*self.submit_button).click
        time.sleep(3)

    