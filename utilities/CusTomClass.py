from selenium.webdriver.common.by import By

class CustomClass():
    def __init__(self,driver):
        self.driver =driver
    def getType(self,LocatorType):
        LocatorType=LocatorType.lower()
        if LocatorType == 'id':
            return By.ID
        elif LocatorType =='xpath':
            return  By.XPATH
        else:
            print("No any path is"+LocatorType)
    def getElement(self,locator,LocatorType='id'):
        element =None
        try:
            LocatorType=LocatorType.lower()
            byType=self.getType(LocatorType)
            element=self.driver.find_element(byType,locator)
            print("Element Found")
        except:
            print("Element No Found")
        return element



