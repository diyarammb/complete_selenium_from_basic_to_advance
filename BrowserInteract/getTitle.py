import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
class getTitle():
    def gettitlevalue(self):
        baseurl='https://facebook.com/'
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseurl)

        titleval= driver.title
        time.sleep(3)
        print("Title of Page is",titleval)

ob =getTitle()
ob.gettitlevalue()