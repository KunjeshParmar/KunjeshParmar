import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME, "name").send_keys("Kunjesh")
driver.find_element(By.NAME, "email").send_keys('test@gmail.com')
driver.find_element(By.ID, 'exampleInputPassword1').send_keys('123456')
driver.find_element(By.ID, "exampleCheck1").click()

# xpath- //tagname[@attribute=value], //input[@type='submit']
# CSS- tagname[attribute=value], div[class='alert alert-success alert-dismissible']
# Css- for CSS we can also use-: #id, .classname
driver.find_element(By.XPATH, '//input[@type="submit"]').click()
msg=driver.find_element(By.CSS_SELECTOR,"div[class='alert alert-success alert-dismissible']").text
print(msg)

assert "successfully" in msg

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(" Parmar")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

time.sleep(5)