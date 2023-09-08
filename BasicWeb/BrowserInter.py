from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class BrowserInter():
    def test(self):
        baseurl='https://www.letskodeit.com/'
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)
        clickFeild=driver.find_element(By.XPATH,"//a[@href='/login']")
        clickFeild.click()
        time.sleep(3)
        email =driver.find_element(By.ID,"email")
        email.send_keys("dayakarma48@gmail.com")
        passfield=driver.find_element(By.ID,"login-password")
        passfield.send_keys("12345!")
        # logedin=
        driver.find_element(By.ID,'login').click()
        time.sleep(5)



ob=BrowserInter()
ob.test()
