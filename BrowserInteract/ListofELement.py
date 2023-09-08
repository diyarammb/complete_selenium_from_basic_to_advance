from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class ListofELements():
    def test(self):
        baseUrl="https://www.letskodeit.com/practice"
        drivers=webdriver.Chrome()
        drivers.maximize_window()
        drivers.get(baseUrl)
        drivers.implicitly_wait(10)

        SelectRadio=drivers.find_elements(By.XPATH,"//input[contains(@type,'radio') and contains(@name,'cars')]")
        size =len(SelectRadio)
        print("size of Elments is",str(size))
        for btn in SelectRadio:
            sbtn = btn.is_selected()
            if not sbtn:
                btn.click()
                time.sleep(2)


ob=ListofELements()
ob.test()