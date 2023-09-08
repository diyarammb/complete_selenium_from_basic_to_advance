from selenium import  webdriver
from selenium.webdriver.common.by import By

class ListofElemnt():
    def listElemtnt(self):
        baseUrl ='https://www.letskodeit.com/practice'
        drivers=webdriver.Chrome()
        drivers.get(baseUrl)
        drivers.implicitly_wait(10)

        ListofTag =drivers.find_element(By.TAG_NAME,"input")

        if ListofTag is not None:

            print("Size of element is " )
        ListofClass =drivers.find_element(By.CLASS_NAME,"btn-style")

        if ListofClass is not None:

            print("Size of these Element is ")
run_test=ListofElemnt()
run_test.listElemtnt()

