import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(2)
driver.get("https://www.google.com")
print(driver.title)
driver.find_element(By.NAME, 'q').send_keys("naveen automationlabs")
time.sleep(1)
ele = driver.find_elements(By.CSS_SELECTOR,'ul.G43f7e li')

for i in ele:
    print(i.text)
    if i.text== 'naveen automationlabs youtube':
        i.click()
        break

time.sleep(5)

