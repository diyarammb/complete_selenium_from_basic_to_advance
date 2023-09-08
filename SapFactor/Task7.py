import time
from gspread import Cell
from Login import *
import  gspread
class Task7():
    Login()
    curl = driver.current_url
    d = curl.split("=")[-1]
    rurl = "https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=%s"
    rate_url = rurl % d
    driver.get(rate_url)

    def object_analye(self):
        sa = gspread.service_account()
        sh = sa.open('Net2apps')
        ws_8 = sh.get_worksheet(8)
        hw.getElement("19__write_toggle","id").click()
        time.sleep(1)
        hw.getElement('//a[@title="Object Definition"]','xpath').click()
        time.sleep(1)
        hw.getElement("9__write_toggle", "id").click()
        elements = hw.getdropDown("//table[@class='MDFSearchBar']//tr//td[contains(text(),'Search')]/following-sibling::td[1]/span[3]//input",'xpath','id')
        time.sleep(1)
        durl = driver.current_url
        u = durl.split("=")[-2]
        id=1
        index=0
        cell_list = []
        for i in elements[:15]:
            key=i['code']
            url = (f'https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=%s=1&t=GOObjectDefinition&i={key}')
            con_url = url % u
            driver.get(con_url)
            time.sleep(2)
            title = hw.GetElementText('//div[@class="ectFCTitle"]', 'xpath')
            col=2
            id += 1
            index+=1
            cell_list.append(Cell(row=id, col=2, value=title))
            cell_list.append(Cell(row=id, col=1, value=index))
            for v in range(1,15):
                col += 1
                val = hw.GetElementText(f'(//td[@class="field_value"])[{v}]', 'xpath')
                cell_list.append(Cell(row=id, col=col, value=val))
        ws_8.update_cells(cell_list)


ob =Task7()
ob.object_analye()
