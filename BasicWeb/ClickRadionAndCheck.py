from selenium import  webdriver
from selenium.webdriver.common.by import  By
import  time
class ClickRadioCheck():
    def radiocheck(self):
        baseUrl="https://www.letskodeit.com/practice"
        drivers=webdriver.Chrome()
        drivers.maximize_window()
        drivers.get(baseUrl)
        drivers.implicitly_wait(10)

        radioCheck=drivers.find_element(By.ID,"bmwradio")
        radioCheck.click()
        time.sleep(3)
        checkBox =drivers.find_element(By.ID,'bmwcheck')
        checkBox.click()
        time.sleep(3)

ob=ClickRadioCheck()
ob.radiocheck()
