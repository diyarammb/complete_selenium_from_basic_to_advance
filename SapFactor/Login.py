from selenium import  webdriver
import time
from Task.Handy import Handy
baseUrl = 'https://pmsalesdemo8.successfactors.com'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)
driver.implicitly_wait(10)
hw=Handy(driver)
def Login():

    search = hw.getElement("//input[@id='__input0-inner']", "xpath")
    search.send_keys("SFPART065417")
    time.sleep(1)
    login = hw.getElement("//span[@id='__button0-img']", "xpath")
    login.click()
    time.sleep(1)
    email = hw.getElement("//input[@id='__input1-inner']", "xpath")
    email.send_keys("codebotintern")
    time.sleep(1)
    password = hw.getElement("__input2-inner", "id")
    password.send_keys("partBos@DC8@@")
    time.sleep(1)
    hw.getElement("__button2-inner", "id").click()
    time.sleep(1)
    hr=hw.GetElementText('//div[@data-testid="children"]','xpath')
    print(hr)


