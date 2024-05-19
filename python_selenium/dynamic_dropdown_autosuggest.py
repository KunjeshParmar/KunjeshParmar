import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(2)

countries=driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")

for country in countries:
    if country.text == "India":
        country.click()
        break


# print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"


time.sleep(2)