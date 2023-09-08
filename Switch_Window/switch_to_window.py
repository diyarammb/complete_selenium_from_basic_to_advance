import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

class SwitchToWindow():
    def windowswichTo(self):
        baseurl='https://www.letskodeit.com/practice'
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        element=driver.find_element(By.ID,'openwindow')
        element.click()
        handle_p=driver.current_window_handle
        handles=driver.window_handles

        for handle in handles:
            print("All handles"+handle)
            if handle not  in handle_p:
                driver.switch_to.window(handle)
                print("switch window"+handle)
                searchBox=driver.find_element(By.XPATH,"//input[@id='search']")
                searchBox.send_keys("python")
                time.sleep(3)
                driver.close()
                break

ob =SwitchToWindow()
ob.windowswichTo()