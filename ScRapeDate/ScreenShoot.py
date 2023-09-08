import time

from selenium import  webdriver
from  selenium.webdriver.common.by import By
class ScreenShoot():
    def take_screen(self):
        baseUrl='https://www.letskodeit.com/login'
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        driver.find_element(By.ID,"email").send_keys("acb@gmail.com")
        driver.find_element(By.ID,'login-password').send_keys("123456")
        driver.find_element(By.ID,'login').click()
        time.sleep(3)
        self.test(driver)

    def test(self,driver):
        try:
            fileName =str(round(time.time()*1000))+".png"
            destinations = "C:\\Users\Daya\\Desktop\\"
            destinationsFile =destinations+fileName
            driver.save_screenshot(destinationsFile)
            print("Save ScreentShoot"+destinationsFile)
        except NotADirectoryError:
            print("No directory Issue")


ob =ScreenShoot()
ob.take_screen()
