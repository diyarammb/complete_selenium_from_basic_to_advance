from selenium import  webdriver
from selenium.webdriver.common.by import By
import  time

from selenium.webdriver.support.select import Select


class DropDownSelect():
    def selectDrop(self):
        baseUrl='https://www.letskodeit.com/practice'
        driver=webdriver.Chrome()

        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        element=driver.find_element(By.ID,'carselect')
        sel=Select(element)
        b=sel.select_by_value('benz')
        print("Select Benz",b)
        time.sleep(2)
        for i in range(3):
            v= sel.select_by_index(i)
            print("slect Honda by Index",v)
            time.sleep(2)


ob = DropDownSelect()
ob.selectDrop()