import time

class PageIndex:
    def __init__(self,myDriver):
        self.driver = myDriver

    def click_register(self):
        self.driver.find_element_by_link_text("REGISTER").click()

    def login(self,user_name,password):
        user_box = self.driver.find_element_by_name('userName').send_keys(user_name)
        pass_box = self.driver.find_element_by_name('password').send_keys(password)
        submit_button = self.driver.find_element_by_name('login').click()
        time.sleep(3)

    