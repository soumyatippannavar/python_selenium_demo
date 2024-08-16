import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

option = Options()
option.add_argument('--allow-running-insecure-content')
option.add_argument('--ignore-certificate-error')
#option.headless=True
driver = webdriver.Chrome(options = option)
driver.get("https://expired.badssl.com/")

driver.maximize_window()
driver.implicitly_wait(10)
webele = driver.find_element(By.ID,"details-button")

webele.screenshot(".\\button1.png")
time.sleep(3)

driver.get_screenshot_as_file("C:\\Users\\EI12548\\selenium\\amazon1.png")
time.sleep(2)
