import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/")
driver.maximize_window()
# using link text
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
# xpath, using parent to child travel
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
# css, using parent to child travel
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Demo@1234")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys("Demo@1234")
# xpath, using text() method
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()



time.sleep(5)
