import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
class DateSelection():
    def selected_date(self):
        baseurl='https://www.expedia.com'
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseurl)
        clickCale=driver.find_element(By.ID,"d1-btn")
        clickCale.click()
        # selecDate=driver.find_element(By.XPATH,"//button[contains(@data-day,'22') and contains(@aria-label,'Jul')][1]")
        # selecDate.click()
        self.DateS=driver.find_element(By.XPATH,"//button[contains(@data-stid,'apply-date-picker')and contains(text(),'Done')]")
        self.DateS.click()
        time.sleep(3)
        driver.quit()



ob=DateSelection()
ob.selected_date()