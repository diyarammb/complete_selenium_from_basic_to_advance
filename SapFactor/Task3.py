import time
from gspread_formatting import *
from Login import *
import  gspread
from Task.Handy import Handy
def Validate():
        Login()
        hw=Handy(driver)
        sa = gspread.service_account()
        sh = sa.open('Net2apps')
        ws = sh.get_worksheet(5)
        red = CellFormat(
            backgroundColor=Color(1, 0, 0),)
        green = CellFormat(
            backgroundColor=Color(0, 1, 0) )
        curl = driver.current_url
        d = curl.split("=")[-1]
        rurl = "https://pmsalesdemo8.successfactors.com/acme?fbacme_o=admin&pess_old_admin=true&ap_param_action=form_rating_scale&itrModule=talent&_s.crb=%s"
        rate_url = rurl % d
        driver.get(rate_url)
        heading=ws.col_values(2)[1:]

        value = ws.get_all_records()
        for v in value:
              if v['Status'] == "Pending":
                  element=hw.isElementPresent(f"//a[.='{v['Rating Scale Name']}']", "xpath")
                  element.click()
                  time.sleep(1)
                  try:
                        hw.isElementPresent("//button[@name='OK']", "xpath").click()
                        time.sleep(1)
                  except:
                      print('No Ok')

                  score = hw.GetElementlistofattributeText(
                      '//table[@id = "66:m-m-tbl"]//tr//span[contains(@title, "numerical value")]//input', 'xpath',
                      'value')
                  size = len(score)

                  for i in range(0,size):
                       sCheck = hw.isElementPresent(f"//span[@title='The numerical value used for rating calculations,"
                                                   f" for example 3.0.']//input[@value='{v['Score']}']", 'xpath')
                       label=hw.isElementPresent(f"//div[@class='gridCell']//span[@title='The short title or abbreviation of the rating increment. For example, Meets Expectations.']//input[@value='{v['Score Label']}']",
                            'xpath')
                       i+=1
                       if element==False:
                          format_cell_range(ws,f'B{v["ID"]+i}',red)
                       else:
                         format_cell_range(ws, f'B{v["ID"]+i}', green)

                       if sCheck==False:
                           format_cell_range(ws, f'D{v["ID"] + i}', red)
                       else:
                           format_cell_range(ws, f'D{v["ID"] + i}', green)
                       if label==False:
                           format_cell_range(ws, f'E{v["ID"] + i}', red)
                       else:
                           format_cell_range(ws, f'E{v["ID"] + i}', green)

              v["Status"] = 'Processed'
              ws.update_acell(f'I{v["ID"] + 1}', 'Processed')


Validate()