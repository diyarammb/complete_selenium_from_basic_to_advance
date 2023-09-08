import time

from  selenium import  webdriver
from selenium.webdriver.common.by import By

class AlertWindow():
    def alertPopup(self):
        baseurl="https://www.letskodeit.com/practice"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)
        alertOk=driver.find_element(By.ID,"alertbtn")
        alertOk.click()
        time.sleep(2)
        alert1=driver.switch_to.alert
        alert1.accept()
        time.sleep(2)
        driver.find_element(By.ID,"confirmbtn").click()
        time.sleep(2)
        alert2=driver.switch_to.alert
        alert2.dismiss()
        time.sleep(2)

ob=AlertWindow()
ob.alertPopup()