from  selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.common.exceptions import *

import  time

class ExplicityWait():
    def ExplicityM(self):
        # baseurl="https://www.letskodeit.com"
        driver=webdriver.Chrome()
        driver.maximize_window()
        # driver.get(baseurl)
        driver.execute_script("window.location='https://www.letskodeit.com'")
        # login =driver.find_element(By.XPATH,"//a[@href='/login']").click()
        wait=WebDriverWait(driver,timeout=10,poll_frequency=1,ignored_exceptions=[
                                                                                    NoSuchDriverException,
                                                                                    ElementNotVisibleException,
                                                                                    ElementNotSelectableException])
        element=wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/login']")))
        element.click()

        time.sleep(2)
        driver.quit()
ob =ExplicityWait()
ob.ExplicityM()
