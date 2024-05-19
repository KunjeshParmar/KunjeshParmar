import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
items= driver.find_elements(By.XPATH, "//div[@class='products']/div")

# grab name of products.
prod= driver.find_elements(By.XPATH, "//div/h4[@class='product-name']")

count=len(items)

assert count > 0

# validating list items
prodlist=[]
for x in prod:
    prodlist.append(x.text)
print(prodlist)

actualList= ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']


assert actualList == prodlist


for item in items:
    item.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//a/img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//div/button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div/span[@class='promoInfo']")))
text=driver.find_element(By.XPATH, "//div/span[@class='promoInfo']").text
assert text == "Code applied ..!"

#driver.find_element(By.XPATH, "//div/div/button[text()='Place Order']").click()

# Functional testing.
values= driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum=0
for value in values:
    sum= sum+ int(value.text)
print(sum)

total= int(driver.find_element(By.XPATH, "//div/span[@class='totAmt']").text)
disamount = float(driver.find_element(By.XPATH, "//div/span[@class='discountAmt']").text)
print("after discount: ", disamount)
#print(type(disamount))

assert sum == total
assert total > disamount

