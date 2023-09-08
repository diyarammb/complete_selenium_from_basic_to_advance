from Login import *
from Model_MDF_Object import *
from Controller_MDF_Object import Controller_Object
from works_sheet import works_sheet
from Config_MDF_Object import Config

class TC_REVERSE_MDF_OBJECT():
    Login()
    config = Config()
    row = 1
    def excute_process(self):
        self.config.red_url(driver, hw)
        elements = hw.getdropDown(
            "//table[@class='MDFSearchBar']//tr//td[contains(text(),'Search')]/following-sibling::td[1]/span[3]//input",
            'xpath', 'id')
        time.sleep(1)
        durl = driver.current_url
        u = durl.split("=")[-2]

        for i in elements[:12]:
            self.object_process(u,i['code'])
    def object_process(self,u,key):
        url = (
            f'https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=%s=1&t=GOObjectDefinition&i={key}')
        con_url = url % u
        driver.get(con_url)
        time.sleep(1)
        text_path="//span[@class='text' and contains(text(),'{0}')]//parent::span//parent::td//following-sibling::td/div/span/span/following-sibling::span"
        obj_list = []
        self.row = self.row + 1
        obj=Model_Object()
        obj.id=self.row
        obj.code=hw.GetElementText(text_path.format('Code'),"xpath")
        obj.Effective=hw.GetElementText(text_path.format('Effective Dating'),"xpath")
        obj.Visibility=hw.GetElementText(text_path.format('API Visibility'),"xpath")
        obj.Status=hw.GetElementText(text_path.format('Status'),"xpath")
        obj.History=hw.GetElementText(text_path.format('MDF Version History'),"xpath")
        obj.Screen=hw.GetElementText(text_path.format('Default Screen'),"xpath")
        obj.Label=hw.GetElementText(text_path.format('Label'),"xpath")
        obj.Description=hw.GetElementText(text_path.format('Description'),"xpath")
        obj.Version=hw.GetElementText(text_path.format('API Sub Version'),"xpath")
        obj.Subject=hw.GetElementText(text_path.format('Subject User Field'),"xpath")
        obj.Workflow=hw.GetElementText(text_path.format('Workflow Routing'),"xpath")
        obj.Pending=hw.GetElementText(text_path.format('Pending Data'),"xpath")
        obj.Todo=hw.GetElementText(text_path.format('Todo Category'),"xpath")
        obj.Object=hw.GetElementText(text_path.format('Object Category'),"xpath")
        obj.Secured=hw.GetElementText(text_path.format('Secured'),"xpath")
        obj.Permission=hw.GetElementText(text_path.format('Permission Category'),"xpath")
        obj.RBP=hw.GetElementText(text_path.format('RBP Subject User Field'),"xpath")
        obj.Criteria=hw.GetElementText(text_path.format('CREATE Respects Target Criteria'),"xpath")
        obj.Blocking=hw.GetElementText(text_path.format('Base Date Field For Blocking'),"xpath")
        obj_list.append(obj)

        ws=works_sheet('Reverse-CDO')
        controller=Controller_Object()
        controller.fill_worksheet(ws,obj_list,self.row)



ob=TC_REVERSE_MDF_OBJECT()
ob.excute_process()







