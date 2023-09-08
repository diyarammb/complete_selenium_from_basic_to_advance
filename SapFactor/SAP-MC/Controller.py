from Model import *
from  gSheet import ws_con
from SapFactor.Login import *
ws_5=ws_con(5)
class Control_model():
        def Controller(self):
            value = ws_5.get_all_records()
            list_data=[]
            pending_element_list=[]
            for i in value:
                a=Model_Rating_Scale()
                a.id=i['ID']
                a.Scale_Name=i['Scale Name']
                a.Scale_Description=i['Scale Description']
                a.Score=i['Score']
                a.Score_Label=i['Score Label']
                a.Score_Description=i['Score Description']
                list_data.append(a)
                # pending elemnenets objects
                p=Processing_Status()
                p.Heading=i['Rating Scale Name']
                p.Status=i['Status']
                pending_element_list.append(p)
            PendingElement=[v.Heading for v in pending_element_list if v.Status=="Pending"]
            ProcessingElements=[j for j in list_data if j.Scale_Name in PendingElement]
            self.Process_Elements(ProcessingElements)

        def Process_Elements(self,ProcessingElements):
            Login()
            curl = driver.current_url
            d = curl.split("=")[-1]
            rurl = "https://pmsalesdemo8.successfactors.com/acme?fbacme_o=admin&pess_old_admin=true&ap_param_action=form_rating_scale&itrModule=talent&_s.crb=%s"
            rate_url = rurl % d
            driver.get(rate_url)
            for a in ProcessingElements:
                element = hw.isElementPresent(f"//a[.='{a.Scale_Name}']", "xpath")
                element.click()
                time.sleep(1)
                try:
                    hw.isElementPresent("//button[@name='OK']", "xpath").click()
                    time.sleep(1)
                except:
                    print('No Ok')
                sCheck = hw.isElementPresent(f"//span[@title='The numerical value used for rating calculations,"
                                             f" for example 3.0.']//input[@value='{a.Score}", 'xpath')
                label = hw.isElementPresent(
                    f"//div[@class='gridCell']//span[@title='The short title or abbreviation of the rating increment. For example, Meets Expectations.']//input[@value='{a.Score_Label}']",
                    'xpath')
                if element == False:
                    format_cell_range(ws_5, f'B{a.id + 1}', red)
                else:
                    format_cell_range(ws_5, f'B{a.id + 1}', green)
                if sCheck == False:
                    format_cell_range(ws_5, f'C{a.id + 1}', red)
                else:
                    format_cell_range(ws_5, f'C{a.id + 1}', green)
                if label == False:
                    format_cell_range(ws_5, f'D{a.id + 1}', red)
                else:
                    format_cell_range(ws_5, f'D{a.id + 1}', green)


                hw.getElement("//span[@class=' icon icon_cancel']", "xpath").click()
                time.sleep(1)



ob=Control_model()
ob.Controller()







