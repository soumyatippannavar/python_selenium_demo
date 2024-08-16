import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Drop_down:
    def Dropdown(self):
        driver = webdriver.Chrome()
        driver.get("https://www.orangehrm.com/en/30-day-free-trial")
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.find_element(By.NAME,"Name").send_keys("harish")
        time.sleep(2)
        webele = driver.find_element(By.CSS_SELECTOR,'select#Form_getForm_Country')

        print(webele.get_attribute('class'))
        driver.implicitly_wait(10)
        sel = Select(webele)   #------using select class #
        list_country = sel.options
        print(len(list_country))

        #for ele in list_country:
            #print(ele.text)
            #print(ele)
        #time.sleep(10)

        sel.select_by_index(1)
        time.sleep(2)

        #driver.find_element(By.)
        driver.switch_to.frame(1)
        time.sleep(1)
        driver.find_element(By.XPATH,"//span[@id='recaptcha-anchor']/div[@class='recaptcha-checkbox-border']").click()
        time.sleep(3)

dd = Drop_down()
dd.Dropdown()