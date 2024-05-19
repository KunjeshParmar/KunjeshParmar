import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.maximize_window()
driver.switch_to.frame("//frame[@name='frame-left']")
print(driver.find_element(By.XPATH, "//frame[@name='frame-left']").text)

