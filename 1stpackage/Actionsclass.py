import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.get("https://www.easemytrip.com/airline-tickets/spicejet.html")
driver.maximize_window()
driver.implicitly_wait(10)

Login = driver.find_element(By.XPATH, "//span[text()='My Account']")
#time.sleep(2)
##Dropdown = driver.find_element(By.LINK_TEXT, "My Booking")
time.sleep(5)
print(Login.text)
