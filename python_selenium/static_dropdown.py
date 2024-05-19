import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

dropdown=Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
#dropdown.select_by_index(1)
#dropdown.select_by_value()
dropdown.select_by_visible_text("Female")

time.sleep(5)
