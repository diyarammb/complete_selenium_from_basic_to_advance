from selenium.webdriver.common.by import By
import time
class w3Method():
    def __init__(self,driver):
        self.driver=driver

    def getType(self,locatorType):
        locatorType=locatorType.lower()
        if locatorType=='id':
            return By.ID
        elif locatorType=='xpath':
            return By.XPATH

# get element method
    def getElement(self,locator,locatorType):
        element=None
        try:
            locatorType = locatorType.lower()
            byType=self.getType(locatorType)
            element=self.driver.find_element(byType,locator)
            # print("element Found")
        except:
            print("element not found")
        return element

    def getElements(self, locator, locatorType):
        elements = []
        try:
            byType = self.getType(locatorType)
            elements = self.driver.find_elements(byType, locator)

        except:
            print("elements not found")
        return elements
    def clickElement(self,locator,locatorType='xpath'):
        try:
            btn=self.getElement(locator,locatorType)
            btn.click()
        except:
            print("element not cliked")

    def getTextbyElement(self,locator,locatorType):
        textval=None
        try:
            textval=self.getElement(locator,locatorType)

        except:
            print("Text not found ")
        return textval
    def getTextByElements(self,locator,locatorType):
        textvalues=[]
        try:
            txt=self.getElements(locator,locatorType)
            time.sleep(1)
            for i in txt:
                textvalues.append(i)

        except:
            print("text elements not found")
        return textvalues
    def GetElementAttribute(self,locator,locatorType,attribute):
        try:
            attribute=self.getElement(locator,locatorType).get_attribute(attribute)
            print(attribute)
        except:
            print(attribute+"is not present in the tag")
        return attribute
    def GetElementlistofattributeText(self,locator,locatorType,attribute):
        att = []
        try:
            attributes=self.getElements(locator,locatorType)

            for i in attributes:
                val=i.get_attribute(attribute)
                att.append(val)
                print(val)

        except:
            print("list of attributes no found")
        return att








