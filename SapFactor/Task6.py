import time
import  gspread
from  Login import  *
class AutomatedSap():
    Login()
    def sheet_automat(self):

        curl = driver.current_url
        d = curl.split("=")[-1]
        rurl = "https://pmsalesdemo8.successfactors.com/acme?fbacme_o=admin&pess_old_admin=true&ap_param_action=form_rating_scale&itrModule=talent&_s.crb=%s"
        rate_url = rurl % d
        driver.get(rate_url)
        time.sleep(2)
        sa = gspread.service_account()
        sh = sa.open('Net2apps')
        ws = sh.get_worksheet(6)
        values = ws.get_all_records()
        status=ws.col_values(9)[1:]
        title=ws.col_values(8)[1:]
        for i , s in enumerate(status):
            if s == "Pending":
                v=title[i]
                element = hw.isElementPresent(f"//a[.='{v}']", "xpath")
                element.click()
                time.sleep(1)
                try:
                    hw.ClickElement("//button[@name='OK']", "xpath")
                    time.sleep(1)
                except:
                    pass
                time.sleep(1)
                id=0
                for j in values:
                    if j['Scale Name'] == v:
                        id+=1
                        score=hw.getElement(f'(//table[@id = "66:m-m-tbl"]//tr//span[contains(@title, "numerical value")]//input)[{id}]','xpath')
                        label=hw.getElement(f'(//table[@id = "66:m-m-tbl"]//tr//span[contains(@title, "title or abbreviation")]//input)[{id}]','xpath')
                        des=hw.getElement(f'(//table[@id = "66:m-m-tbl"]//tr//span[contains(@title, "The description")]//textarea)[{id}]','xpath')
                        score.clear()
                        score.send_keys(j['Score'])
                        label.clear()
                        label.send_keys(j['Score Label'])
                        des.clear()
                        des.send_keys(j['Score Description'])

                hw.getElement('//span[@class=" icon icon_save"]', 'xpath').click()
                time.sleep(1)
                hw.getElement("//span[@class=' icon icon_cancel']", "xpath").click()
                time.sleep(1)


ob=AutomatedSap()
ob.sheet_automat()