import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
driver.implicitly_wait(2)


def click_on(element, values):
    for ele in List_of_ele:
        print(ele.text)
        for K in range(len(values)):
            if ele.text == values[K]:
                ele.click()
                break


driver.find_element(By.XPATH, "//div[@class='ui-dropdown-trigger ui-state-default ui-corner-right ng-tns-c65-12']").click()

time.sleep(10)

List_of_ele = driver.find_elements(By.CSS_SELECTOR, 'span.ng-star-inserted')

List_of_values = ['LADIES', 'GENERAL']

click_on(List_of_ele, List_of_values)

time.sleep(5)