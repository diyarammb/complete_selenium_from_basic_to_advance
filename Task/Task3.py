from selenium import webdriver
from Task.Handy import Handy
class Task3():
    def task(self):
        baseurl = "https://www.w3schools.com/python/default.asp"
        driver = webdriver.Chrome()
        driver.maximize_window()
        hw = Handy(driver)
        driver.get(baseurl)
        driver.implicitly_wait(3)


        title = {}
        subtitle = []
        txt = input("Enter Title")
        elements = hw.getElements(f"//div[@id='leftmenuinnerinner']//h2[.='{txt}']//following-sibling::*","xpath")
        for i in elements:
            tag = i.tag_name
            title[txt]=list()
            if tag == 'a':
                subtitle.append(i.text)

            elif tag == 'h2' or tag == 'br':
                break
            else:
                continue
        title[txt] = subtitle
        print(title)
         






ob = Task3()
ob.task()