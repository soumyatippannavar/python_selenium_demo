import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.orangehrm.com/en/30-day-free-trial")
driver.maximize_window()
driver.implicitly_wait(20)


def general(lists, value):
    for ele in lists:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break


Elements = driver.find_elements(By.XPATH, '//*[@id="Form_getForm_Country"]/option')
general(Elements, "India")
time.sleep(10)
