import time
from selenium import webdriver

driver = webdriver.Chrome('driver/chromedriver.exe')
driver.get('https://www.google.com/')
time.sleep(20)

search_box = driver.find_element_by_name("q").send_keys("dracula")
