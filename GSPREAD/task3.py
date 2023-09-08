import time
from gspread_formatting import  *
from selenium import webdriver
from Task.Handy import Handy
import gspread

class Task3():
    sa = gspread.service_account()
    sh = sa.open("Net2apps")
    baseurl = "https://www.w3schools.com"
    driver = webdriver.Chrome()
    driver.maximize_window()
    hw = Handy(driver)
    driver.get(baseurl)
    driver.implicitly_wait(4)
    ws = sh.get_worksheet(3)

    def dataValidation(self):
        fmt = CellFormat(backgroundColor=Color(0, 1, 0))
        fmt1 = CellFormat(backgroundColor=Color(1,0, 0))

        status=self.ws.col_values(7)
        all_rows = self.ws.get_values()

        for i in status:
            if i =="Pending":
                ind = status.index('Pending')
                Heading=self.ws.get_values(f'F{ind+1}')
                HeadingValues = self.ws.col_values(2)
                [[val]]=Heading
                item = HeadingValues.index(val)
                data=all_rows[item:]
                id=1
                for j in data:
                    [x1, x2, x3, x4, x5, x6,x7] = j

                    if [[x2]]==Heading:
                        try:
                            atrList = x4.split('https://www.w3schools.com')
                            stringAtr = ''.join(atrList)
                        except:
                            stringAtr=x4
                        H=self.hw.getElement(f"//h5[.='{x2}']", "xpath")
                        if H is not None:
                            format_cell_range(self.ws , f'B{item+id}', fmt)
                            time.sleep(1)
                        else:
                            format_cell_range(self.ws , f'B{item+id}', fmt1)
                            time.sleep(1)
                        S=self.hw.getElement(f"//h5[.='{x2}']//parent::*//parent::div//a[.='{x3}']", "xpath")
                        if S==None:
                            format_cell_range(self.ws, f'C{item + id}', fmt1)
                            time.sleep(1)
                        else:
                            format_cell_range(self.ws, f'C{item + id}', fmt)
                            time.sleep(1)
                        L = self.hw.getElement(f"//h5[.='{x2}']//parent::*//parent::div//a[@href='{stringAtr}']", "xpath")
                        if L==None:
                            format_cell_range(self.ws, f'D{item + id}', fmt1)
                            time.sleep(1)
                        else:
                            format_cell_range(self.ws, f'D{item + id}', fmt)
                            time.sleep(1)
                        id += 1
                else:  pass
                status[ind]='Processed'
                self.ws.update_acell(f'G{ind + 1}', 'Processed')


ob = Task3()
ob.dataValidation()


