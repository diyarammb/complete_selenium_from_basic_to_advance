from selenium import webdriver
from Task.Handy import Handy
import csv
class Task4():
    def task(self):
        baseurl = "https://www.w3schools.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        hw = Handy(driver)
        driver.get(baseurl)
        driver.implicitly_wait(3)
        driver.execute_script("window.scrollBy(0,15000);")


        Heading={}
        Subheadings=[]
        SubHeadingLink=""
        txtI=input(" Enter Heading")
        sub=input('Enter Sub Heading')
        s=hw.GetElementText(f"//div[@class='top10']//a[contains(text(),'{sub}')]","xpath")
        elements = hw.getElements(f"//div[@class='top10']//h5[contains(text(),'{txtI}')]//following-sibling::*",'xpath')
        link=hw.GetElementByAttribute(f"//div[@class='top10']//a[contains(text(),'{sub}')]",'xpath','href')
        for i in elements:
            tag = i.tag_name
            Heading[txtI]=list()
            if tag =="a":
                Subheadings.append(i.text)
            elif tag =="h5":
                break
            else:
                continue

         # for sub heaing links


        if sub == s:
            SubHeadingLink=link




        Heading[txtI]=txtI
        Heading['Subheadings']=sub
        Heading['SubheadingLinks']=SubHeadingLink

        print(Heading)

ob = Task4()
ob.task()