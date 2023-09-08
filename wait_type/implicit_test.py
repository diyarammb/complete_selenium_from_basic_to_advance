import  time
from utilities.DriverClass import DriverWeb
from selenium.webdriver.common.by import By
class ImplicityWait(DriverWeb):
    def ImplWait(self):
        email=DriverWeb.driver.find_element(By.ID,"email")
        email.send_keys("deve")
        time.sleep(2)



ob =ImplicityWait()
ob.ImplWait()

