from selenium import  webdriver
from selenium.webdriver.common.by import  By

class FindByLink():
     def byLink(self):
         Baseurl='https://www.letskodeit.com/practice'
         driver=webdriver.Chrome()
         driver.get(Baseurl)
         driver.implicitly_wait(10)

         FindByTextLink = driver.find_element(By.LINK_TEXT,"HOME")
         if FindByTextLink is not None:
             print("Text Founded  by LinkTes")

         partialLink = driver.find_element(By.PARTIAL_LINK_TEXT,"Courses")
         if partialLink is not None:
             print("Partial link Found by Text")

run_test=FindByLink()
run_test.byLink()