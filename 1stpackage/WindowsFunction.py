import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.get("https://www.easemytrip.com/airline-tickets/spicejet.html")
driver.maximize_window()
driver.implicitly_wait(10)
Login = driver.find_element(By.XPATH, "//a[@class='_btnclick']")
time.sleep(5)
print(Login.text)
action = ActionChains(driver)

action.move_to_element(Login).perform()
Dropdown = driver.find_element(By.XPATH,"//*[@id='divSignInPnl']/div/a[4]")
time.sleep(5)

Dropdown.click()
time.sleep(5)



