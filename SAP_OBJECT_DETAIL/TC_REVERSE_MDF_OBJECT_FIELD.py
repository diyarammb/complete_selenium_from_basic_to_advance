import time

from Login import *
from Config_MDF_Object_Field import Config_MDF_Field
from Model_MDF_Object_Field import Model_Details_Field
from SAP_Object_Def.works_sheet import works_sheet
from CONTROLLER_MDF_OBJECT_FIELD import CONTROLLER_MDF_OBJECT_FIELD
from gspread import Cell


class TC_REVERSE_MDF_OBJECT_FIELD():
        Login()
        Config =Config_MDF_Field()
        row=1
        ws = works_sheet('CDO_Field_Validate')
        def excute_process(self):
                self.Config.red_url(driver,hw)
                elements = hw.getdropDown(
                        "//table[@class='MDFSearchBar']//tr//td[contains(text(),'Search')]/following-sibling::td[1]/span[3]//input",
                        'xpath', 'id')
                time.sleep(1)
                durl = driver.current_url
                u = durl.split("=")[-2]
                id=1

                for i in elements[:3]:
                        id+=1
                        key=i['code']
                        self.ws.update_cell(id,26,key)
                        self.process_Object(key,u)

        def process_Object(self,key,u):
                url = (
                        f'https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=%s=1&t=GOObjectDefinition&i={key}')
                con_url = url % u
                driver.get(con_url)
                time.sleep(1)
                path = '//td[@class="field_label"]//label[.="{0}"]//parent::td//following-sibling::td//span[@class="readonly readComp"]'
                path2 = '(//td[@class="field_label"]//label[.="{0}"]//parent::td//following-sibling::td//span[@class="readonly read_only"])[1]'

                field_list=[]
                controller = CONTROLLER_MDF_OBJECT_FIELD()

                elements=hw.GetElementlistofattributeText("(//span[@class='form_title']//parent::div//following-sibling::div[@class='layoutFieldsContainer']//table//label[.='Name'])[1]//parent::th//parent::tr//following-sibling::tr//label[.='Name']//parent::span//input",'xpath','value')

                for e in elements[:22]:
                        link=hw.getElement(f"(//td//span[.='{e}']//parent::*//parent::*//parent::*//following-sibling::td//a[.='Details'])[2]",'xpath')
                        link.click()
                        time.sleep(0.5)
                        obj=Model_Details_Field()
                        self.row = self.row + 1
                        obj.Object=key
                        obj.Name=hw.GetElementText(path.format('Name'),'xpath')
                        obj.Database=hw.GetElementText(path2.format('Database Field Name'),'xpath')
                        obj.Maximum_Length=hw.GetElementText(path.format('Maximum Length'),'xpath')
                        obj.Data_Type=hw.GetElementText(path.format('Data Type'),'xpath')
                        obj.Valid_Values_Source=hw.GetElementText(path.format('Valid Values Source'),'xpath')
                        obj.Hide_Old_Value=hw.GetElementText(path.format('Hide Old Value'),'xpath')
                        obj.Decimal_Precision=hw.GetElementText(path.format('Decimal Precision'),'xpath')
                        obj.Include_Inactive_Users=hw.GetElementText(path.format('Include Inactive Users'),'xpath')
                        obj.UI_Field_Renderer=hw.GetElementText(path.format('UI Field Renderer'),'xpath')
                        obj.Transient=hw.GetElementText(path.format('Transient'),'xpath')
                        obj.Help_Text=hw.GetElementText(path.format('Help Text'),'xpath')
                        obj.Mask_Value=hw.GetElementText(path.format('Mask Value on UI'),'xpath')
                        obj.Show_Trailing=hw.GetElementText(path.format('Show Trailing Zeros'),'xpath')
                        obj.Default_Value=hw.GetElementText(path.format('Default Value'),'xpath')
                        obj.Hide_Seconds=hw.GetElementText(path.format('Hide Seconds'),'xpath')
                        obj.Required=hw.GetElementText(path.format('Required'),'xpath')
                        obj.Visibility=hw.GetElementText(path.format('Visibility'),'xpath')
                        obj.Status=hw.GetElementText(path.format('Status'),'xpath')
                        obj.Label=hw.GetElementText(path.format('Label'),'xpath')
                        obj.Cascade=hw.GetElementText(path.format('Cascade'),'xpath')
                        obj.Inactivated_By=hw.GetElementText(path2.format('Inactivated By'),'xpath')
                        obj.End_Period=hw.GetElementText(path2.format('End Of Period'),'xpath')
                        field_list.append(obj)
                        controller.fillworksheet(self.ws,field_list,self.row)
                        hw.ClickElement('//button[@title="Done"]','xpath')
                        time.sleep(1)




ob=TC_REVERSE_MDF_OBJECT_FIELD()
ob.excute_process()