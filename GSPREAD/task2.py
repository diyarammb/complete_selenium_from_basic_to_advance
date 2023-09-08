import time

from gspread import Cell
from gspread_formatting import DataValidationRule, BooleanCondition, set_data_validation_for_cell_range
from selenium import webdriver
from Task.Handy import Handy
import gspread

class Task1():
    sa = gspread.service_account()
    sh = sa.open("Net2apps")
    baseurl = "https://www.w3schools.com/python/default.asp"
    driver = webdriver.Chrome()
    driver.maximize_window()
    hw = Handy(driver)
    driver.get(baseurl)
    driver.implicitly_wait(4)
    ws = sh.get_worksheet(2)

    def ReverseData(self):
        id=1
        item=2
        HeadingOfElement = self.hw.GetElementlistofText("//div[@class='w3-row w3-center w3-small']//h5", "xpath")
        for i in HeadingOfElement:
            self.ws.update_cell(item, 6, i)

            subHeading = self.hw.GetElementlistofText(f"//div[@class='w3-row w3-center w3-small']//*[.='{i}']/following-sibling::a",
                                          "xpath")

            for j in subHeading:
                id+=1
                subLink = self.hw.getElement(f"//a[.='{j}']", "xpath")
                LinkVar = subLink.get_attribute("href")
                cell_list = [
                        Cell(row=id, col=2, value=i),
                        Cell(row=id, col=3, value=j),
                        Cell(row=id, col=4, value=LinkVar),
                    ]

                self.ws.update_cells(cell_list)
                ValidationRule = DataValidationRule(
                    BooleanCondition('ONE_OF_LIST', ['Pending', 'Processed']),
                    showCustomUi=True
                )
                set_data_validation_for_cell_range(self.ws, 'G2:G5', ValidationRule)
                time.sleep(1)

            item +=1



ob = Task1()
ob.ReverseData()


