from selenium import  webdriver
import  time
from selenium.webdriver.common.by import By
from Task.methods import w3Method


class Task2():
    def test2(self):
        baseurl = 'https://www.w3schools.com/python/default.asp'
        driver = webdriver.Chrome()
        driver.maximize_window()
        tw = w3Method(driver)
        driver.implicitly_wait(3)
        driver.get(baseurl)

        print("========HEADING============")
        head=tw.getTextByElements("//div[@id='leftmenuinnerinner']//h2","xpath")
        for i in head:
            print(i.text)

        print("========Enter Title for check sub heading ============");txt = input("")

        print("========SubHeading============")

        elements = tw.getElements(f"//div[@id='leftmenuinnerinner']//h2[contains(text(),'{txt}')]//following-sibling::*", "xpath")
        for i in elements:
            tag = i.tag_name
            if tag == 'a':
                print(i.text)
            elif tag == 'h2' or tag == 'br':
                break
            else:
                continue


ob=Task2()
ob.test2()