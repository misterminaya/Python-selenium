import time
from selenium import webdriver

driver = webdriver.Chrome('driver/chromedriver.exe')
driver.get('http://newtours.demoaut.com')

time.sleep(10)
user_box = driver.find_element_by_name('userName').send_keys('test')
pass_box = driver.find_element_by_name('password').send_keys('test')
submit_button = driver.find_element_by_name('login').click()
time.sleep(5)
driver.quit()

