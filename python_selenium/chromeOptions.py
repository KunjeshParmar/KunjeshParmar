from selenium import webdriver

chrome_options= webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--ignore-certificate-errors')

#important for ChromeOptions= https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions

driver= webdriver.Chrome(options=chrome_options)


driver.get("https://rahulshettyacademy.com/")
print(driver.title)