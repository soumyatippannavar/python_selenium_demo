import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
browser = "Edge"
if browser == "chrome":
    driver = webdriver.Chrome()
    time.sleep(2)
elif browser == "Edge":
    driver = webdriver.Edge()
else:
    print("browser name is:" + browser)


driver.get("https://www.google.com")
print(driver.title)


