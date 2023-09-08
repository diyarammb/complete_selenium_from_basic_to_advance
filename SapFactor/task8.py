import time
from gspread_formatting import *
from Login import *
import gspread
class Task8():
    Login()
    curl = driver.current_url
    d = curl.split("=")[-1]
    rurl = "https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=%s"
    rate_url = rurl % d
    driver.get(rate_url)
    def object_analye(self):
        red = CellFormat(
            backgroundColor=Color(1, 0, 0), )
        green = CellFormat(
            backgroundColor=Color(0, 1, 0))
        sa = gspread.service_account()
        sh = sa.open('Net2apps')
        ws_9 = sh.get_worksheet(9)
        hw.ClickElement("19__write_toggle", "id")
        time.sleep(1)
        hw.ClickElement('//a[@title="Object Definition"]', 'xpath')
        time.sleep(1)
        hw.ClickElement("9__write_toggle", "id")
        time.sleep(2)
        values=ws_9.get_all_records()
        for v in values:
                if v['Status-sap']=='Pending':
                    durl = driver.current_url
                    u = durl.split("=")[-2]
                    url = (
                        f'https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=%s=1&t=GOObjectDefinition&i={v["Code"]}')
                    con_url = url % u
                    driver.get(con_url)
                    time.sleep(2)
                    title =hw.isElementPresent('//div[@class="ectFCTitle"]', 'xpath')

                    if title== False:
                        format_cell_range(ws_9,f'B{v["ID"]+1}:',red)
                        time.sleep(1)
                    else:
                        format_cell_range(ws_9, f'B{v["ID"] + 1}', green)
                        time.sleep(1)
                    # if v['Code'] is not None:
                    #     format_cell_range(ws,f'C{v["ID"]+1}:',green)
                    #     time.sleep(1)
                    # else:
                    #     format_cell_range(ws, f'C{v["ID"] + 1}', red)
                    #     time.sleep(1)
                    # if v['Effective Dating'] is not None:
                    #     format_cell_range(ws,f'D{v["ID"]+1}:',green)
                    #     time.sleep(1)
                    # else:
                    #     format_cell_range(ws, f'D{v["ID"] + 1}', red)
                    #     time.sleep(1)
                    # if v['API Visibility'] is not None:
                    #     format_cell_range(ws,f'E{v["ID"]+1}:',green)
                    #     time.sleep(1)
                    # else:
                    #     format_cell_range(ws, f'E{v["ID"] + 1}', red)
                    #     time.sleep(1)
                    # if v['status'] is not None:
                    #     format_cell_range(ws, f'F{v["ID"] + 1}:', green)
                    #     time.sleep(1)
                    # else:
                    #     format_cell_range(ws, f'F{v["ID"] + 1}', red)
                    #     time.sleep(1)
                    #
                    # if v['MDF Version History'] is not None:
                    #     format_cell_range(ws, f'G{v["ID"] + 1}:', green)
                    #     time.sleep(1)
                    # else:
                    #     format_cell_range(ws, f'G{v["ID"] + 1}', red)
                    #     time.sleep(1)
                    # # if v['Default Screen'] is not None:
                    # #     format_cell_range(ws, f'H{v["ID"] + 1}:', green)
                    # #     time.sleep(1)
                    # # else:
                    # #     format_cell_range(ws, f'H{v["ID"] + 1}', red)
                    # #     time.sleep(1)
                    # v["Status"] = 'Processed'
                    # ws.update_acell(f'Q{v["ID"]+1}', 'Processed')
ob = Task8()
ob.object_analye()
