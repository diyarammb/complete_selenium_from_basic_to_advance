import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class HotWire():
    def hotWireData(self):
        baseUr="https://www.hotwire.com/"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUr)
        driver.implicitly_wait(10)

        SignIn=driver.find_element(By.XPATH,"//button[@data-bdd='sign-in']")
        SignIn.click()
        email=driver.find_element(By.ID,"email")
        email.send_keys("dayakarma48@gmail.com")
        Upass=driver.find_element(By.ID,"password")
        Upass.send_keys("8tTBL4.dMkL-UXz")
        time.sleep(2)
        LogedIn=driver.find_element(By.XPATH,"//button/span[contains(@class,'btn__label btn__label--truncate') and contains(text(),'Sign In')]")
        LogedIn.click()
        time.sleep(60)
ob =HotWire()
ob.hotWireData()


