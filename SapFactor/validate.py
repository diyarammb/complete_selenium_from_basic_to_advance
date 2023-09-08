import time
from gspread_formatting import *
import  gspread
from Login import *
class Validations():
    def SapValidate(self):

        red = CellFormat(
            backgroundColor=Color(1, 0, 0), )
        green = CellFormat(
            backgroundColor=Color(0, 1, 0))
        sa = gspread.service_account()
        sh = sa.open('Net2apps')
        ws = sh.get_worksheet(5)
        values=ws.get_all_records()
        status=ws.col_values(9)[1:]
        title=ws.col_values(8)[1:]
        for c, i in enumerate(status):
            v=title[c]
            if i == 'Pending':

                link = login.hw.getElement(f"//a[.='{v}']", "xpath")
                link.click()
                time.sleep(2)
                for j in values:
                     if j['Scale Name'] == v:
                         format_cell_range(ws, f'B{j["ID"]+1}', green)
                         time.sleep(1)
                c += 2
                status[c] = 'Processed'
                ws.update_acell(f'I{c}', 'Processed')


                login.hw.getElement("//span[@class=' icon icon_cancel']", "xpath").click()
                time.sleep(1)



ob =Validations()
ob.SapValidate()