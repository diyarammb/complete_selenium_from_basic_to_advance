import time

from selenium import  webdriver
from Handy import  Handy

class Wrapper():
    def test(self):
        baseurl = "https://www.letskodeit.com/practice"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw=Handy(driver)
        driver.get(baseurl)

        # hw.ClickElement("//div[contains(@id,'category-list') and contains(text(),'Topics')]",locatorType='xpath')
        # time.sleep(1)

        # hw.GetElementlistofText("//ul[@id='category-list-topics']",locatorType='xpath')
        # time.sleep(1)
        # hw.IsElementPresent("//ul[@id='category-list-topics']",locatorType='xpath')
        # hw.GetElementByAttribute("//ul[@id='category-list-topics",locatorType='xpath',attribute='a')
        hw.GetElementlistofattributeText("alertbtn",locatorType='id',attribute='class')




ob=Wrapper()
ob.test()

