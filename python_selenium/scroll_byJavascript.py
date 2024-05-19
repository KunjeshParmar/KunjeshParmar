import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()

# scroll by as per given height
#driver.execute_script("window.scrollBy(0,500)")

# scroll by bottom of page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

time.sleep(2)
