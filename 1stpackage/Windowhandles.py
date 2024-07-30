import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.orangehrm.com/en/30-day-free-trial")
parentwindow = driver.current_window_handle
driver.implicitly_wait(10)
driver.maximize_window()
driver.execute_script("window.scrollBy(0,500)","")
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Privacy Policy")
time.sleep(2)
link.click()
time.sleep(3)
windowhandle = driver.window_handles

for i in windowhandle:
    if i != parentwindow:
       driver.switch_to.window(i)
       driver.close()
       time.sleep(1)

time.sleep(3)
driver.switch_to.window(parentwindow)
time.sleep(3)
Facebook_link = driver.find_element(By.XPATH,'//img[@alt="facebook logo"]')
driver.execute_script("window.scrollBy(0,1000)","")
time.sleep(2)
Facebook_link.click()
time.sleep(2)
handle = driver.window_handles
for i in handle:
    if i != parentwindow:
       driver.switch_to.window(i)
       driver.close()
       time.sleep(2)
driver.switch_to.window(parentwindow)
time.sleep(3)
driver.execute_script("window.scrollBy(1000,0)","")
time.sleep(2)