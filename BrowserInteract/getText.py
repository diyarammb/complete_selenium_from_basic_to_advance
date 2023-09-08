from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
class getText():
    def textGet(self):
        baseUrl='https://www.letskodeit.com/practice'
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        gettext=driver.find_elements(By.ID,'opentab')
        content=gettext.text

        print("The Text value on"+content)

ob=getText()
ob.textGet()
