import time
from selenium import webdriver

driver = webdriver.Chrome('driver/chromedriver.exe')
driver.get('http://newtours.demoaut.com')

time.sleep(5)
user_box = driver.find_element_by_name('userName').send_keys('test')
pass_box = driver.find_element_by_name('password').send_keys('test')
submit_button = driver.find_element_by_name('login').click()
time.sleep(3)


#validar ciertos caracteres de una prueba
link_registration_form = driver.find_element_by_link_text("registration form")
assert link_registration_form.text == "registration form"
print("Complete test")


driver.quit()


