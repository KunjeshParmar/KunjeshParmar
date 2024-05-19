import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

name="Kunjesh"
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()
# switch to alert
alert=driver.switch_to.alert
time.sleep(2)
alertText=alert.text
print(alertText)
assert name in alertText
#alert.accept()
alert.dismiss()

time.sleep(3)