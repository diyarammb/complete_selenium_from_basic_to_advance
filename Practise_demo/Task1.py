import time

from selenium import  webdriver
from selenium.webdriver.common.by import By


class Task1():
    def test1(self):
        baseURl="https://www.pof.com"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURl)
        driver.implicitly_wait(6)

        searchDomain=driver.find_element(By.XPATH,"//input[@name='domainToCheck']")
        searchDomain.send_keys("Dayadeveloper.com")
        time.sleep(2)
        clickDomain=driver.find_element(By.XPATH,"//button[@data-creative-name='search_button']").click()
        time.sleep(5)


ob1=Task1()
ob1.test1()

