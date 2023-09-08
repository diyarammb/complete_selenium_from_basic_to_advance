import time
import  pandas as pd
from selenium import  webdriver
from selenium.webdriver.common.by import  By

class ScrapeData():
    def Data(self):
        baseUrl='https://www.goibibo.com'
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)
        partialTExt="Del"
        textSelect="New Delhi, India"



        textElement=driver.find_element(By.XPATH,"//div[@class='sc-12foipm-34 dVpEne']")
        textElement.click()

        Element=driver.find_element(By.XPATH,'//div[@class="sc-12foipm-37 godvBN"]//input')
        Element.send_keys(partialTExt)
        time.sleep(2)
        ulElement=driver.find_element(By.ID,"autoSuggest-list")
        inner_html=ulElement.get_attribute("innerHTML")
        # print(inner_html)
        time.sleep(2)

        liElement=ulElement.find_elements(By.TAG_NAME,"li")
        time.sleep(3)
        data=[]

        for element in liElement:
            data.append(element.text)
            # print(element.text)
            # if textSelect in element.text:
            #     element.click()
            #     break

        df = pd.DataFrame(data, columns=['city_name'])

        df.to_csv('cities_location.csv', index=False, sep=";")
        time.sleep(2)




ob =ScrapeData()
ob.Data()