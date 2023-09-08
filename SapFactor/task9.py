import time
from Login import *
import gspread
class Task8():
    Login()
    def object_analye(self):
        sa = gspread.service_account()
        sh = sa.open('Net2apps')
        ws = sh.get_worksheet(9)
        hw.ClickElement("19__write_toggle", "id")
        time.sleep(2)
        hw.ClickElement('//a[@title="Object Definition"]', 'xpath')
        time.sleep(2)
        hw.ClickElement("9__write_toggle", "id")
        time.sleep(2)
        value=ws.get_all_records()
        durl = driver.current_url
        u = durl.split("=")[-2]
        for i in value:
            if i['Status'] == 'Pending':
                key=i['Code']
                url = (
                    f'https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=%s=1&t=GOObjectDefinition&i={key}')
                con_url = url % u
                driver.get(con_url)
                time.sleep(5)
                hw.ClickElement('//button[@aria-label="Take Action"]','xpath')
                time.sleep(1)
                hw.ClickElement('//a[@title="Make Correction"]','xpath')
                time.sleep(2)

                code=hw.getElement('(//input[@class="formElement  fd-input fd-input--compact"])[1]','xpath')
                code.clear()
                code.send_keys(i['Code'])
                time.sleep(2)
                try:
                    hw.ClickElement('//button[@title="OK"]', 'xpath')
                    time.sleep(1)
                except:
                    print('l')

                hw.ClickElement('//button[@title="OK"]', 'xpath')
                time.sleep(1)

                hw.getElement('(//span[@class="fd-input-group__addon fd-input-group__addon--compact fd-input-group__addon--button toggle"])[3]','xpath').click()
                time.sleep(2)
                hw.ClickElement(f'//a[.="None"]','xpath')
                time.sleep(2)
                print(hw.GetElementText('//div[@class="mdfErrorMsgList"]', 'xpath'))
                hw.ClickElement('//span[@id="27472__write_toggle"]','xpath')
                time.sleep(1)
                hw.ClickElement('//a[.="Editable"]','xpath')
                time.sleep(2)

                label=hw.getElement('(//input[@class="formElement  fd-input fd-input--compact"])[2]','xpath')
                subject=hw.getElement('(//input[@class="formElement  fd-input fd-input--compact"])[3]','xpath')
                des=hw.getElement(f'//textarea[@class="formElement ectTextArea hideScrollbar fd-textarea fd-textarea--compact"]', 'xpath')

                label.clear()
                des.clear()
                subject.clear()

                subject.send_keys(i['Subject User Field'])
                label.send_keys(i['Label'])
                des.send_keys(i['Description'])
                time.sleep(1)
                hw.ClickElement('//button[@title="Save"]','xpath')
                time.sleep(3)
                try:
                    hw.ClickElement('//div[@class="buttonLayout fd-bar__right fd-bar__right--compact"]//button[@title="Yes"]', 'xpath')

                except:
                    print('no save')
                try:
                    hw.ClickElement('//button[@title="OK"]', 'xpath')
                    time.sleep(1)
                except:
                   print('finally:')
                time.sleep(2)
#

ob = Task8()
ob.object_analye()
