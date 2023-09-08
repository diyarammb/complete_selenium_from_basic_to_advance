import time
from Controller_MDF_Object import Controller_Object
from works_sheet import works_sheet
from Config_MDF_Object import Config
from Login import *

class TC_AUTOMATIONS_MDF_Object():
    Login()
    config = Config()
    ws =works_sheet('CDO_automate')

    def excute_process(self):
        data_list=self.ws.get_all_records()
        controller=Controller_Object()
        pending_data=controller.Load_data(data_list)
        self.config.red_url(driver,hw)
        durl = driver.current_url
        u = durl.split("=")[-2]
        for v in pending_data:
            self.object_process(v,u)
    def object_process(self,data,u):
        url = (
        f'https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=%s=1&t=GOObjectDefinition&i={data.code}')
        con_url = url % u
        driver.get(con_url)
        time.sleep(0.3)
        text_path ='(//span[@class="text" and contains(text(),"{0}")]//parent::span//parent::td//following-sibling::td//input//following-sibling::span)[2]'
        d_ele='(//li[@role="option"])[1]//a'
        list_ele='//a[@titile="{0}"]'
        attribute='//span[@class="text" and contains(text(),"{0}")]//parent::span//parent::td//following-sibling::td//input'


        hw.ClickElement('//button[@aria-label="Take Action"]', 'xpath')
        time.sleep(1)
        hw.ClickElement('//a[@title="Make Correction"]', 'xpath')
        time.sleep(1)
        element=data.Screen


        hw.static_dropdown_click(attribute.format('Effective Dating'),'xpath',value=data.Effective,listel=list_ele.format(data.Effective),iconclick=text_path.format('Effective Dating'))
        hw.static_dropdown_click(attribute.format('API Visibility'),'xpath',value=data.Visibility,listel=list_ele.format(data.Visibility),iconclick=text_path.format('API Visibility'))
        hw.static_dropdown_click(attribute.format('Status'),'xpath',value=data.Status,listel=list_ele.format(data.Status),iconclick=text_path.format('Status'))
        hw.static_dropdown_click(attribute.format('MDF Version History'),'xpath',value=data.History,listel=list_ele.format(data.History),iconclick=text_path.format('MDF Version History'))
        hw.dynamic_dropdown_click(attribute.format('Default Screen'),'xpath',value=data.Screen,sendK=d_ele)
        hw.fill_field(attribute.format('Label'),'xpath',keys=data.Label)
        hw.fill_field('//div[@class="writeComp ectTextAreaWrapper"]//textarea', 'xpath', keys=data.Description)
        hw.static_dropdown_click(attribute.format('API Sub Version'),'xpath',value=data.Version,listel=list_ele.format(data.Version),iconclick=text_path.format('API Sub Version'))
        hw.static_dropdown_click(attribute.format('Subject User Field'),'xpath',value=data.Subject,listel=list_ele.format(data.Subject),iconclick=text_path.format('Subject User Field'))
        hw.dynamic_dropdown_click(attribute.format('Workflow Routing'), 'xpath', value=data.Workflow, sendK=d_ele)
        hw.static_dropdown_click(attribute.format('Pending Data'),'xpath',value=data.Pending,listel=list_ele.format(data.Pending),iconclick=text_path.format('Pending Data'))
        hw.static_dropdown_click(attribute.format('Object Category'),'xpath',value=data.Object,listel=list_ele.format(data.Object),iconclick=text_path.format('Object Category'))
        hw.static_dropdown_click(attribute.format('Secured'),'xpath',value=data.Secured,listel=list_ele.format(data.Secured),iconclick=text_path.format('Secured'))
        hw.dynamic_dropdown_click(attribute.format('Permission Category'), 'xpath', value=data.Permission, sendK=d_ele)
        hw.fill_field(attribute.format('RBP Subject User Field'),'xpath',keys=data.RBP)
        hw.static_dropdown_click(attribute.format('CREATE Respects Target Criteria'),'xpath',value=data.Criteria,listel=list_ele.format(data.Criteria),iconclick=text_path.format('CREATE Respects Target Criteria'))
        hw.fill_field(attribute.format('Base Date Field For Blocking'),'xpath',keys=data.Blocking)

        hw.ClickElement('//button[@name="Save"]', 'xpath')
        time.sleep(0.3)
        hw.popup('//div[@class="mdfErrorMsgList"]','xpath')
        time.sleep(0.3)




ob =TC_AUTOMATIONS_MDF_Object()
ob.excute_process()
