import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Dragable():
    def dropElement(self):
        baseurl="https://jqueryui.com/droppable/"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)
        driver.switch_to.frame(0)

        fromElement=driver.find_element(By.XPATH,"//div[contains(@id,'draggable')]")
        toElement=driver.find_element(By.XPATH,"//div[contains(@id,'droppable')]")

        try:
            actions=ActionChains(driver)
            Performaction = actions.click_and_hold(fromElement).move_to_element(toElement)
            Performaction.release().perform()
            print("Drag and Drop Element Successfully ")
            time.sleep(2)
        except:
            print("Something Not Working")

ob=Dragable()
ob.dropElement()
