import time
import  pandas as pd

from selenium import  webdriver
from selenium.webdriver.common.by import By

class Task2():
    def test2(self):
        baseURl = "https://help.pof.com/hc/en-us"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURl)
        driver.implicitly_wait(6)
        time.sleep(2)
        ques = "Member Communication & Profile"
        driver.find_element(By.XPATH,"//div[contains(@id,'category-list') and contains(text(),'Topics')]").click()
        ulList=driver.find_element(By.XPATH,"//ul[@id='category-list-topics']")
        innerHTM=ulList.get_attribute("innerHTML")
        time.sleep(2)
        # print(innerHTM)
        liement=ulList.find_elements(By.TAG_NAME,"a")
        time.sleep(3)
        driver.find_element().get_attribute()
        quizlist=[]
        for i in liement:
            quizlist.append(i.text)





        time.sleep(5)
        df = pd.DataFrame(quizlist, columns=['quiz'])

        df.to_csv('quizlist.csv',index=False,sep=";")










ob=Task2()
ob.test2()