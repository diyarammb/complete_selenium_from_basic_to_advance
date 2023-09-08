import time
from selenium.webdriver.common.by import By
from selenium import  webdriver
class Handy():
    def __init__(self,driver):
        self.driver=driver
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
        elif locatorType=='class':
            return By.CLASS_NAME
        else:
            print("this "+locatorType +"doesn`t exit")
    def getElement(self,locator,locatorType):
        element=False
        try:
            locatorType=locatorType.lower()
            byType=self.getType(locatorType)
            element=self.driver.find_element(byType,locator)
            # if element is not None:
                # print("Element found")
            # else:
            #     print("element not found")

        except:
            print("this locator type is not in "+locatorType+"type")
        return element

    def getElements(self,locator,locatorType):
        list_element=[]
        try:
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
             if itemList is not None:
                 # print("Elements found")
                 for i in itemList:
                     list_of_text.append(i.text)
             # else:
             #     print("ELements Not Found")
        except:
            print("list of text not found")
        return  list_of_text



    def isElementPresent(self, locator, locatortype):
        element = self.getElement(locator, locatortype)
        if element not in [None, False]:
            return True
        else:
            return False





    def GetElementByAttribute(self,locator,locatorType,attribute):
        attributes=None
        try:
            attributes=self.getElement(locator,locatorType).get_attribute(attribute)
            # print("attribute found " + attribute)
        except:
            print(" attribute not found")
        return attributes
    def GetElementlistofattributeText(self,locator,locatorType,attribute):
        attributes_list = []
        try:
           listofElemente = self.getElements(locator, locatorType)
           for i in listofElemente:
                atributeVal=i.get_attribute(attribute)
                attributes_list.append(atributeVal)
        except:
                print("attributes list not exits in given attributes")
        return  attributes_list
    def fill_field(self,locator,locatorType,keys):
        element=self.getElement(locator,locatorType)
        if element.text==keys:
            pass
        else:
            element.clear()
            element.send_keys(keys)
    def getdropDown(self,locator,locatorType,attribute):

        objects_list_dict=[]
        try:
            searchBox_id = str(self.GetElementByAttribute(locator,locatorType,attribute)).split("__")[0] + "_"
            self.driver.execute_script(
                "ECTUtil.getComponentById('" + searchBox_id + "')._model._searchFields.pageSize = 2000")
            objects_list_dict = self.driver.execute_script(
                "return ECTUtil.getComponentById('" + searchBox_id + "')._model._searchDAO._staticData.results;")
        except:
            print("no Drop down Elements")

        return objects_list_dict

    def static_dropdown_click(self,locator,locatorType,value,iconclick,listel):
        element=self.GetElementByAttribute(locator,locatorType,'value')
        try:
            if element!= value:
                self.ClickElement(iconclick,locatorType)
                time.sleep(0.2)
                self.ClickElement(listel,locatorType)

            else:
                pass
        except:
            print('incorrect input ')


    def dynamic_dropdown_click(self, locator,locatorType,value,sendK):
        element=self.GetElementByAttribute(locator,locatorType,'title')
        try:
            if element!=value:

                self.fill_field(locator,locatorType,keys=value)
                time.sleep(1)
                self.ClickElement(sendK, locatorType)
                time.sleep(1)
            else:
                pass


        except:
            print('incorrect input ')
    def popup(self,locator,locatorType):
        try:
            element=self.GetElementText(locator,locatorType)
            print(element)
            self.ClickElement('//button[@title="OK"]', locatorType)
        except:
            print('nothing popup')















