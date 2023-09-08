import time

from selenium import webdriver
from Handy_wrapper import HandyWrap

class UsingWrapper():
    def test(self):
        baseurl='https://www.letskodeit.com/practice'
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(6)
        hw=HandyWrap(driver)
        driver.get(baseurl)


        textfield=hw.getElemet("autosuggest",locatorType='id')
        # textfield.send_keys('autosuggest')

        time.sleep(2)


ob=UsingWrapper()
ob.test()
