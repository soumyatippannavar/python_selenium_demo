import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.amazon.com")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@alt="Shop Kitchen favorites"]').click()
time.sleep(2)

cookies = driver.get_cookies()

for cook in cookies:
    print(cook)
time.sleep(3)
driver.back()
time.sleep(2)
driver.forward()
