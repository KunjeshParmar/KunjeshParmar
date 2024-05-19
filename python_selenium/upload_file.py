from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.implicitly_wait(5)

file_path= "C:/Users/Kunjesh Parmar/Downloads/download.xlsx"

driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
file_input= driver.find_element(By.ID, "fileinput")
file_input.send_keys(file_path)

# using smart x-path (paren to child, child to parent) below.
# //div[text()='Banana']/parent::div/parent::div/div[@id='cell-4-undefined']
fruit_name= "Apple"

price_column= driver.find_element(By.XPATH, "//div[text()='Price']").get_attribute("data-column-id")
actual_price= driver.find_element(By.XPATH, "//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@id='cell-"+price_column+"-undefined']").text
print(price_column)
print(actual_price)
