import time
from Model import *
from gspread_formatting import *
from  ws_config import ws_con
from  Login import *
class Model_Controller():
   red = CellFormat(
        backgroundColor=Color(1, 0, 0),)
   green = CellFormat(
       backgroundColor=Color(0, 1, 0), )


   def excute_method(self):
       try:
          ws_8=ws_con(8)
          values= ws_8.get_all_records()
          data=[]
          processList=[]

          for i in values:
              a = Model_Object()
              a.id=i['id']
              a.code=i['Code']
              a.Label=i['Label']
              a.Description=i['Description']
              a.Effective=i['Effective']
              a.History=i['MDF Version History']
              a.Object=i['Object Category']
              a.Screen=i['Default Screen']
              a.Pending=i['Pending Data']
              a.Subject=i['Subject User Field']
              a.Status=i['Status']
              a.Todo=i['Todo Category']
              a.Version=i['API Sub Version']
              a.Workflow=i['Workflow Routing']
              a.Visibility=i['API Visibility']
              data.append(a)
              # processing ELements
              p = Process_Object()
              p.Heading=i['Code']
              p.Status_sap=i['SF_Status']
              processList.append(p)
          pending_elements = [obj.Heading for obj in processList if obj.Status_sap == "Pending"]
          procesed_elements = [ob for ob in data if ob.code in pending_elements]

          self.Process_Elements(procesed_elements)
       except:
           print('No any pending ELement')

   def Process_Elements(self,procesed_elements):
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
       for i in procesed_elements:
           url = (
               f'https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=%s=1&t=GOObjectDefinition&i={i.code}')
           con_url = url % u
           driver.get(con_url)
           time.sleep(2)
           code =hw.isElementPresent("((//table[@class='layoutTable center_align'])[1]/tbody/tr/td[@class='field_label']//following-sibling::td//span[.='AbsencePayPolicy'])[1]",'xpath')
           if code ==False:
               format_cell_range(ws_con(8), f'C{i.id+1}', self.red)
           else:
               format_cell_range(ws_con(8), f'C{i.id+1}', self.green)





ob=Model_Controller()
ob.excute_method()