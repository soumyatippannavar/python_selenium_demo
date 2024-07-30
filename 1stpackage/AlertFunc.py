import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, "input.signinbtn").click()
time.sleep(5)
print("new code added")

alt = Alert(driver)

#alert = driver.switch_to.alert
print(alt.text)
alt.accept()
time.sleep(3)
