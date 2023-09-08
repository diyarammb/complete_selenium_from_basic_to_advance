from gspread import Cell
from selenium import webdriver
from Task.Handy import Handy
from gspread_formatting import  *
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



    def dataInsert(self):
        fmt = CellFormat(backgroundColor=Color(0, 1, 0))
        fmt1 = CellFormat(backgroundColor=Color(1, 0, 0))
        id=1
        r=1
        HeadingOfElement = self.ws.col_values(6)

        status = self.ws.col_values(7)
        for s in status:

            if s=="Pending":
                i=status.index("Pending")
                x = self.ws.cell(r, 6).value
                subHeading = self.hw.GetElementlistofText(
                    f"//div[@class='w3-row w3-center w3-small']//*[.='{x}']/following-sibling::a",
                    "xpath")
                for j in subHeading:
                    id += 1
                    subLink = self.hw.getElement(f"//a[.='{j}']", "xpath")
                    LinkVar = subLink.get_attribute("href")
                    h = self.ws.cell(id, 6).value
                    # if j==h:
                    #     format_cell_range(self.ws, f'B{id}', fmt)

                    print(h)

            r += 1





ob = Task1()
ob.dataInsert()


