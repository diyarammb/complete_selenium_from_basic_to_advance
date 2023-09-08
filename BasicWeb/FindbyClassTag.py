import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

class FindbyTag():
    def findTag(self):
        baseUrl="https://www.letskodeit.com/practice"
        driver=webdriver.Chrome()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        FindyByClass =driver.find_element(By.CLASS_NAME,"inputs")
        if FindyByClass is not None:
            print("Element Found  by Class")
            FindyByClass.send_keys("Web automations")
        FindyByTag =driver.find_element(By.TAG_NAME,"a")
        if FindyByTag is not None:
            print("Element Found By Tag",FindyByTag.text)
            time.sleep(5)
run_test=FindbyTag()
run_test.findTag()
