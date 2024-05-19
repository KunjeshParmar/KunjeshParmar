import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes=driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for checkbox in checkboxes:
    if checkbox.get_attribute('value') == "option3":
        checkbox.click()
        break

time.sleep(3)
