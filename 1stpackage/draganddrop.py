import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")

driver.maximize_window()
driver.switch_to.frame(0)
time.sleep(1)

src = driver.find_element(By.XPATH,"//div[@id='draggable']")
dest = driver.find_element(By.XPATH,"//div[@id='droppable']")
time.sleep(1)
Act = ActionChains(driver)
#Act.drag_and_drop(src, dest).perform()  #both command will work
Act.click_and_hold(src).release(dest).perform()
time.sleep(3)


