import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
class SwitchWindow():
    def windowSwitch(self):
        baseurl="https://www.letskodeit.com/practice"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        element=driver.find_element(By.ID,"openwindow")
        element.click()
        parentHandle=driver.current_window_handle
        print("Handles are " + parentHandle)
        time.sleep(2)
        handles=driver.window_handles


        for handle in handles:
            print("hadle"+handle)
ob =SwitchWindow()
ob.windowSwitch()