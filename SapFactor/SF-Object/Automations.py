import time
from Model import *
from Login import *
from ws_config import ws_con
class Task10():
    def excute_method(self):
        ws_9=ws_con(9)
        value=ws_9.get_all_records()
        data = []
        for i in value:
            a = Model_Object()
            a.id = i['id']
            a.code = i['Code']
            a.Label = i['Label']
            a.Description = i['Description']
            a.Effective = i['Effective']
            a.History = i['MDF Version History']
            a.Object = i['Object Category']
            a.Screen = i['Default Screen']
            a.Pending = i['Pending Data']
            a.Subject = i['Subject User Field']
            a.Status = i['Status']
            a.Todo = i['Todo Category']
            a.Version = i['API Sub Version']
            a.Workflow = i['Workflow Routing']
            a.Visibility = i['API Visibility']
            data.append(a)
        self.Process_object(data)
    def Process_object(self,data):
        Login()
        # configure object definations page url

        curl = driver.current_url
        d = curl.split("=")[-1]
        rurl = "https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=%s"
        rate_url = rurl % d
        driver.get(rate_url)
        time.sleep(1)

        # click on object definations

        hw.getElement("19__write_toggle", "id").click()
        time.sleep(1)
        hw.getElement('//a[@title="Object Definition"]', 'xpath').click()
        time.sleep(1)
        hw.getElement("9__write_toggle", "id").click()
        time.sleep(1)
        durl = driver.current_url
        u = durl.split("=")[-2]
        for e in data:

            url = (
                f'https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=%s=1&t=GOObjectDefinition&i={e.code}')
            con_url = url % u
            driver.get(con_url)
            time.sleep(2)
            self.automat_instance(e)
    def automat_instance(self,e):
        hw.ClickElement('//button[@aria-label="Take Action"]', 'xpath')
        time.sleep(1)
        hw.getElement('//a[@title="Make Correction"]', 'xpath').click()
        time.sleep(2)
        code = hw.getElement('(//input[@class="formElement  fd-input fd-input--compact"])[1]',
                                        'xpath')
        code.clear()
        code.send_keys(e.code)
        time.sleep(1)






ob = Task10()
ob.excute_method()
