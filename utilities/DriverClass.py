from selenium import  webdriver
from selenium.webdriver.common.by import By

class DriverWeb():
    def __init__(self):
        baseUrl='https://www.letskodeit.com/login'
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        print("Driver Method Called")
