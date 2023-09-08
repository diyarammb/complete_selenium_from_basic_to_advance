import time
from Login import *
from Sheet_Con import *
class Model:
  Login()
  def Excute_Process(self):
        curl = driver.current_url
        d = curl.split("=")[-1]
        rurl = "https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=%s"
        rate_url = rurl % d
        driver.get(rate_url)
        time.sleep(1)
        hw.ClickElement("19__write_toggle", "id")
        time.sleep(1)
        hw.ClickElement('//a[@title="Object Definition"]', 'xpath')
        time.sleep(1)
        hw.ClickElement("9__write_toggle", "id")
        # end  configure object url
        elements = hw.getdropDown(
            "//table[@class='MDFSearchBar']//tr//td[contains(text(),'Search')]/following-sibling::td[1]/span[3]//input",
            'xpath', 'id')
        time.sleep(2)
        durl = driver.current_url
        u = durl.split("=")[-2]
        cell_list = []
        row_id = 1
        id = 1
        for i in elements[:15]:
            key = i['code']
            self.Process_Object(u,key,cell_list,id,row_id)


  def Process_Object(self,u,key,cell_list,id,row_id):

            url = (
            f'https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=%s=1&t=GOObjectDefinition&i={key}')
            con_url = url % u
            driver.get(con_url)
            time.sleep(2)
            title = hw.GetElementText('//div[@class="ectFCTitle"]', 'xpath')
            cell_list.append(Cell(row=id, col=2, value=title))
            cell_list.append(Cell(row=id, col=1, value=row_id))
            row_id+=1
            elements=hw.GetElementlistofText("(//table[@class='layoutTable center_align'])[1]/tbody/tr/td[@class='field_label']//following-sibling::td[@class='field_value']",'xpath')
            col = 2
            for  e in elements:
                col+=1
                cell_list.append(Cell(row=id, col=col, value=e))


            ws_7 = ws_con(7)
            ws_7.update_cells(cell_list)

ob = Model()
ob.Excute_Process()
