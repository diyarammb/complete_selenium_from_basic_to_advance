import time

from selenium import webdriver
from methods import w3Method

class W3school():
    def task1(self):
        baseurl='https://www.w3schools.com'
        driver=webdriver.Chrome()
        driver.maximize_window()
        tw=w3Method(driver)
        driver.implicitly_wait(2)
        driver.get(baseurl)


        tw.clickElement("//a[@title='Tutorials and References']","xpath")

        tw.clickElement("//a[@class='w3-bar-item w3-button acctop-link ga-top-drop ga-top-drop-tut-python']", "xpath")

        tw.clickElement("//a[contains(@href,'python_intro.asp') and contains(text(),'Python Intro')]","xpath")
        time.sleep(1)
        tw.getTextbyElement("//h3[text()='Python Syntax compared to other programming languages']",'xpath')
        # time.sleep(2)
        # tw.GetElementAttribute("//*[@id='footer']/div[2]/div[1]/a",locatorType='xpath',attribute='class')
        # time.sleep(1)
        tw.GetElementlistofattributeText("//*[@id='footer']/div[2]/div[1]/a",'xpath','class')




ob =W3school()
ob.task1()