import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
class Login():
    def test(self):
        baseUrl='https://www.letskodeit.com'
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)
        clickFeild = driver.find_element(By.XPATH, "//a[@href='/login']")
        clickFeild.click()
        userEmail=driver.find_element(By.ID,"email")
        userEmail.send_keys("dayakarma48@gmail.com")
        userPass=driver.find_element(By.ID,"login-password")
        userPass.send_keys('12345!')
        time.sleep(1)
        logedIn=driver.find_element(By.ID,'login').click()
        ClickLink=driver.find_element(By.XPATH,"//a[contains(@class,'dynamic-link') and contains(text(),'ALL COURSES')]")
        ClickLink.click()
        time.sleep(2)
        searchBox=driver.find_element(By.XPATH,"//input[@id='search']")
        searchBox.send_keys("Javascript")
        clickSearch =driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(2)
        _course=driver.find_element(By.XPATH,"//*[ contains (text(), 'JavaScript for beginners' )]")
        _course.click()

ob=Login()
ob.test()
