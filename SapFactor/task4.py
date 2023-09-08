import time
from gspread_formatting import *
import  gspread
from  Login import  *
from Task.Handy import Handy

def SapValidate():
        Login()
        hw = Handy(driver)
        red = CellFormat(
            backgroundColor=Color(1, 0, 0), )
        green = CellFormat(
            backgroundColor=Color(0, 1, 0))
        curl = driver.current_url
        d = curl.split("=")[-1]
        rurl = "https://pmsalesdemo8.successfactors.com/acme?fbacme_o=admin&pess_old_admin=true&ap_param_action=form_rating_scale&itrModule=talent&_s.crb=%s"
        rate_url = rurl % d
        driver.get(rate_url)
        sa = gspread.service_account()
        sh = sa.open('Net2apps')
        ws = sh.get_worksheet(5)
        values=ws.get_all_records()
        status=ws.col_values(9)[1:]
        title=ws.col_values(8)[1:]
        for c, i in enumerate(status):
            v=title[c]
            if i == 'Pending':
                link = hw.getElement(f"//a[.='{v}']", "xpath")
                link.click()
                time.sleep(2)
                for j in values:
                     elementCheck= hw.IsElementPresent(f"//span[@title='The numerical value used for rating calculations, for example 3.0.']//input[@value='{j['Scale Name']}']",'xpath')
                     print(elementCheck)


                c += 2
                status[c] = 'Processed'
                ws.update_acell(f'I{c}', 'Processed')


                hw.getElement("//span[@class=' icon icon_cancel']", "xpath").click()
                time.sleep(1)


SapValidate()