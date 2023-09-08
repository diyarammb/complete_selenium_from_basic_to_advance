from selenium import webdriver
from utilities.CusTomClass import CustomClass
import  time
class UsingCustomeM():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = CustomClass(driver)
        driver.get(baseUrl)
        textField1 = hw.getElement("name")
        textField1.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name']", LocatorType="xpath")
        textField2.clear()
ob=UsingCustomeM()
ob.test()