import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.XPATH, "//a[text()='Shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
# using slicing to merge web_element.
for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Nokia Edge":
        product.find_element(By.XPATH, "//button[@class='btn btn-info']").click()

driver.find_element(By.XPATH, "//a[contains(@class,'btn-primary')]").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='India']")))
driver.find_element(By.XPATH, "//a[text()='India']").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
msg = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Thank you!" in msg



time.sleep(2)