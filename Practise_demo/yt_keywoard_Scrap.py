import time
import  pandas as pd
from  selenium import  webdriver
from selenium.webdriver.common.by import By

class YoutubeData():
    def PyKeyworad(self):
        baseurl="https://www.youtube.com"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(5)

        searchBox=driver.find_element(By.XPATH,"//input[@id='search']")
        searchBox.send_keys("python tutorial in hindhi")
        driver.find_element(By.XPATH,"//button[@id='search-icon-legacy']").click()

        time.sleep(2)
        # list_of_title=driver.find_element(By.)



        # df=pd.DataFrame(python_tutorial,columns=['Top keywaords'])
        # df.to_csv("youtube_seo_keyword.csv",index=False,sep=';')






ob=YoutubeData()
ob.PyKeyworad()