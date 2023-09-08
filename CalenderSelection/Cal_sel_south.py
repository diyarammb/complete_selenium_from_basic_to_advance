import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
class SoutWest():
    def Cal_sel(self):
        baseUrl='https://www.southwest.com'
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        sDate=driver.find_element(By.ID,"LandingAirBookingSearchForm_departureDate").click()
        time.sleep(2)
        allDate=driver.find_elements(By.XPATH,"//button[contains(@aria-label,'July')]")

        time.sleep(2)
        date=[]
        for dateI in allDate:
            date.append(dateI.text)
        print(date)
            # if dateI.text == "13":
            #     dateI.click()
            #     print("slected is")



ob =SoutWest()
ob.Cal_sel()