import time
from selenium.webdriver.common.by import By
class Handy():
    def __init__(self,driver):
        self.driver =driver
    def getType(self,locatorType):
        locatorType=locatorType.lower()
        if locatorType =="id":
            return By.ID
        elif locatorType=='xpath':
            return By.XPATH
        elif locatorType=='name':
            return By.TAG_NAME
        elif locatorType=='css':
            return By.CSS_SELECTOR
        else:
            print("this "+locatorType +"doesn`t exit")
    def getElement(self,locator,locatorType):
        element=False
        try:
            locatorType=locatorType.lower()
            byType=self.getType(locatorType)
            element=self.driver.find_element(byType,locator)

        except:
            print("this locator type is not in "+locatorType+"type")
        return element

    def getElements(self,locator,locatorType):
        list_element=[]
        try:
            locatorType=locatorType.lower()
            gettype=self.getType(locatorType)
            list_element=self.driver.find_elements(gettype,locator)

        except:
            print("this is element of list not exits in "+locatorType)
        return list_element
    def ClickElement(self,locator,locatorType):
        elementclick=False
        try:
            elementclick=self.getElement(locator,locatorType)
            if elementclick not in [None,False]:

                elementclick.click()

        except:
            print("Element not Clicked")
        return elementclick

    def GetElementText(self,locator,locatorType):
        text=""
        try:
            textelment=self.getElement(locator,locatorType)
            if text not in [None,False]:
                text = textelment.text
        except:
            print("these element not found")
        return text

    def GetElementlistofText(self,locator,locatorType):
        list_of_text=[]
        try:
             itemList=self.getElements(locator,locatorType)
             for i in itemList:
                 list_of_text.append(i.text)
        except:
            print("list of text not found")
        return  list_of_text



    def IsElementPresent(self,locator,locatorType='xpath'):
        try:
            el=self.getElement(locator,locatorType)
            if el is not None:
                return True
            else:
                return False
        except:
            print("Element is Not present")
    def GetElementByAttribute(self,locator,locatorType,attribute):
        attributes=None
        try:
            attributes=self.getElement(locator,locatorType).get_attribute(attribute)
            print("attribute found " + attribute)
        except:
            print(" attribute not found")
        return attributes
    def GetElementlistofattributeText(self,locator,locatorType,attribute):

        listofElemente=self.getElements(locator,locatorType)
        attributes_list = []
        try:
           for item in listofElemente:
                attris=item.get_attribute(attribute)
                attributes_list.append(attris)
        except:
                print("attributes list not exits in given attributes")
        return  attributes_list










