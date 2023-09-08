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

        Heading={}
        Subheadings=[]
        SubHeadingLink=[]
        txtI=input("Enter Title")
        elements = hw.getElements(f"//div[@class='top10']//h5[contains(text(),'{txtI}')]//following-sibling::*",'xpath')
        links=hw.GetElementlistofattributeText(f"//div[@class='top10']//h5[contains(text(),'{txtI}')]//following-sibling::a",'xpath','href')
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
        for j in elements:
            t=j.tag_name
            for l in links:
                if t=='h5':
                    break
                else:
                     # print(l)
                    SubHeadingLink.append(l)



        Heading[txtI]=[txtI]
        Heading['Subheadings']=Subheadings
        SubHeadingLink = list(dict.fromkeys(SubHeadingLink))
        Heading['SubheadingLinks']=SubHeadingLink

        print(Heading)

ob = Task4()
ob.task()

