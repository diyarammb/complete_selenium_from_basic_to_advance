import time
from Login import Login
import gspread
class Task10():
    def object_analye(self):
        sa = gspread.service_account()
        sh = sa.open('Net2apps')
        ws = sh.get_worksheet(9)
        call_login = Login()
        call_login.LoginSap()
        call_login.hw.getElement("19__write_toggle", "id").click()
        time.sleep(2)
        call_login.hw.getElement('//a[@title="Object Definition"]', 'xpath').click()
        time.sleep(2)
        call_login.hw.getElement("9__write_toggle", "id").click()
        time.sleep(2)
        value=ws.get_all_records()
        durl = call_login.driver.current_url
        u = durl.split("=")[-2]
        for i in value:
            if i['Status'] == 'Pending':
                key=i['Code']
                url = (
                    f'https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=%s=1&t=GOObjectDefinition&i={key}')
                con_url = url % u
                call_login.driver.get(con_url)
                time.sleep(5)
                call_login.hw.getElement('//button[@aria-label="Take Action"]','xpath').click()
                time.sleep(1)
                call_login.hw.getElement('//a[@title="Make Correction"]','xpath').click()
                time.sleep(2)
                code = call_login.hw.getElement('(//input[@class="formElement  fd-input fd-input--compact"])[1]',
                                                'xpath')
                code.clear()
                code.send_keys("laravel")
                time.sleep(2)
                try:
                    call_login.hw.getElement('//button[@title="OK"]', 'xpath').click()
                    time.sleep(2)
                except:
                    print('No code Changes')
                # call_login.hw.getElement('//button[@title="OK"]', 'xpath').click()
                # time.sleep(2)

                call_login.hw.getElement('//span[@id="60__write_toggle"]','xpath').click()
                time.sleep(5)



ob = Task10()
ob.object_analye()
#
# hw.ClickElement('//button[@title="OK"]', 'xpath')
# time.sleep(0.2)
# hw.ClickElement('//button[@title="OK"]', 'xpath')
# time.sleep(0.3)
# hw.ClickElement(
#     '//span[@class="text" and contains(text(),"Effective Dating")]//parent::span//parent::td//following-sibling::td//input//following-sibling::span[@class="fd-input-group__addon fd-input-group__addon--compact fd-input-group__addon--button toggle"]',
#     'xpath')
# time.sleep(0.3)
# hw.ClickElement('//button[@title="OK"]', 'xpath')
# time.sleep(0.3)
# hw.ClickElement(
#     '//span[@class="text" and contains(text(),"Effective Dating")]//parent::span//parent::td//following-sibling::td//input//following-sibling::span[@class="fd-input-group__addon fd-input-group__addon--compact fd-input-group__addon--button toggle"]',
#     'xpath')
#
# hw.ClickElement(f'//a[@title="{data.Effective}"]', 'xpath')
# time.sleep(0.5)
# hw.ClickElement('//button[@title="OK"]', 'xpath')
# time.sleep(0.3)
