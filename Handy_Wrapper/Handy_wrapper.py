from selenium.webdriver.common.by import By
class HandyWrap():
    def __init__(self,driver):
        self.driver=driver
    def getType(self,locatorType):
        locatorType=locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType=="xpath":
            return By.XPATH
        else:
            print("Given Type is not Exist"+locatorType)
        return False
    def getElemet(self,locator,locatorType='id'):
        element=None
        try:
            locatorType=locatorType.lower()
            byType=self.getType(locatorType)
            element=self.driver.find_element(byType,locator)
            print("Element Found")
        except:
            print("given Locator Type is not Exist"+locatorType)
