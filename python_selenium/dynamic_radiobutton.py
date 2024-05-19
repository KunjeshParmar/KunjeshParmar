import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
radiobuttons=driver.find_elements(By.XPATH, "//input[@type='radio']")

for button in radiobuttons:
    if button.get_attribute("value") == "radio2":
        button.click()
        break

time.sleep(2)