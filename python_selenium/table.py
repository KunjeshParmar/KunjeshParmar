import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

# grabbing the amount against name.
name= driver.find_elements(By.XPATH, "//tr/td[1]")
amount= driver.find_elements(By.XPATH, "//tr/td[2]")

nameList=[]
amountList=[]
for ele in name:
    nameList.append(ele.text)

for i in amount:
    amountList.append(i.text)

print(nameList)
print(amountList)
actualAmount=0

for i in range(len(nameList)):
    for j in range(len(amountList)):
        if nameList[i]== "Potato":
            actualAmount=amountList[i]
            break

print(actualAmount)


