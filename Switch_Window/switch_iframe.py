import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

class SwitchFrame():
    def FrameSwithc(self):
        baseurl="https://www.letskodeit.com/practice"
        driver =webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseurl)
        driver.execute_script("window.scroll(0,1000)")
        # Switch Iframe  Using ID
        # driver.switch_to.frame("courses-iframe")

        # Switch Iframe  Using Name
        # driver.switch_to.frame("iframe-name")
        # Switch Iframe  using Number
        driver.switch_to.frame(0)

        time.sleep(2)

        searchBox=driver.find_element(By.XPATH,"//input[@id='search']")
        searchBox.send_keys("python")
        time.sleep(2)

        driver.switch_to.default_content()
        driver.execute_script("window.scroll(0,-1000);")
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@name='enter-name']").send_keys("iframe switch successfully")
        time.sleep(2)



ob=SwitchFrame()
ob.FrameSwithc()