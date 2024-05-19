import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
# clicking on top deals.
driver.find_element(By.XPATH, "//div/a[text()='Top Deals']").click()

# counting numbers of windows open.
windows= driver.window_handles
# window handling, and switching to next window.
driver.switch_to.window(windows[1])
# click on header to sort the table.
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
# grabbing sorted list.
sortedWebelements= driver.find_elements(By.XPATH, "//tr/td[1]")
sortedTable=[]

for ele in sortedWebelements:
    sortedTable.append(ele.text)

newSorted= sortedTable.copy()
print("sortedTable is: ", sortedTable)

# sorting through python method
newSorted.sort()
print("newSorted is: ", newSorted)
assert sortedTable == newSorted

