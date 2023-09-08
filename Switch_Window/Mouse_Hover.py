import time

from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
class MouseHover():
    def MouseClick(self):
        baseurl="https://www.letskodeit.com/practice"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)
        driver.execute_script("window.scroll(0,600)")

        element=driver.find_element(By.ID,"mousehover")

        try:
            actions= ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse Hovered on ELements")
            time.sleep(2)
            topLink=driver.find_element(By.XPATH,"//a[text()='Top']")
            actions.move_to_element(topLink).click().perform()
            print("Item Cliked")
        except:
            print("Mouse Hover Failed on elment")

ob=MouseHover()
ob.MouseClick()


