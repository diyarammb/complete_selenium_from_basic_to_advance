import time
from selenium import  webdriver
from selenium.webdriver.common.by import By

class ElementState():
    def SateE(self):
        baseUrl="https://www.youtube.com"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)

        driver.implicitly_wait(10)
        search=driver.find_element(By.XPATH,"//input[@id='search']")
        search.send_keys("Python Programming")
        btn =driver.find_element(By.XPATH,"//button[@class='style-scope ytd-searchbox']")
        btn.click()
        time.sleep(5)
ob=ElementState()
ob.SateE()
