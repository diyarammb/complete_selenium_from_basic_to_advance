import time

from selenium import  webdriver
from selenium.webdriver.chrome.service import Service as Service

class RunChromeTest():
    def test(self):
        # using complete path
        # service=Service(executable_path="C:\\Users\Daya\\PycharmProjects\\SeleniumWD\\drivers\\chromedriver.exe")
        # add the path variable
        service = Service()
        driver=webdriver.Chrome(service=service)
        driver.get("https://bmaofficials.com")
        time.sleep(5)


runtest=RunChromeTest()
runtest.test()