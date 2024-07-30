import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

#coption = webdriver.ChromeOptions()
#coption.add_argument("headless")
#driver = webdriver.Chrome(options= coption)
driver = webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
click = driver.find_element(By.XPATH, "//span[text()='right click me']")
time.sleep(5)
action=ActionChains(driver)
action.context_click(click).perform()
time.sleep(5)