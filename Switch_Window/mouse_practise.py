import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import  ActionChains

class mouseffect():
    def mouseElement(self):
        baseurl="https://www.letskodeit.com/practice"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)
        driver.execute_script("window.scroll(0,600)")
        time.sleep(2)

        element=driver.find_element(By.ID,"mousehover")
        try:
            actions=ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse Hover On ELement")
            time.sleep(2)
            TopLink=driver.find_element(By.XPATH,"//a[text()='Reload']")
            actions.move_to_element(TopLink).click().perform()
            time.sleep(2)
        except:
            print("failled")
ob=mouseffect()
ob.mouseElement()
