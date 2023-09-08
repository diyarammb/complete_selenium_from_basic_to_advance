from  selenium import  webdriver
from selenium.webdriver.common.by import  By

class FindElement:
    def Elements(self):
        baseUrl ='https://www.letskodeit.com/practice'
        drivers =webdriver.Chrome()
        drivers.get(baseUrl)
        drivers.implicitly_wait(10)

        ElementById=drivers.find_element(By.ID,"autosuggest")
        if ElementById is not None:
            print(f"Element Found  --> by Id is {ElementById}")
        ElementByName=drivers.find_element(By.NAME,"show-hide")
        if ElementByName is not None:
            print(f"ELement Found --> by Name is {ElementByName}")
run=FindElement()
run.Elements()