from  selenium import  webdriver
from selenium.webdriver.common.by import  By

class FindElement:
    def Xpath(self):
        baseUrl ='https://www.letskodeit.com/practice'
        drivers =webdriver.Chrome()
        drivers.get(baseUrl)
        drivers.implicitly_wait(10)

        ElementByXpath=drivers.find_element(By.XPATH,"//input[@id='enabled-example-input']")
        if ElementByXpath is not None:
            print(f"Element Found  --> by Xpath ")
        ElementByCss=drivers.find_element(By.CSS_SELECTOR,"#enabled-example-input")
        if ElementByCss is not None:
            print(f"ELement Found --> by Css is")
run=FindElement()
run.Xpath()