import time

from SAP_Object_Def.Config_MDF_Object import Config
from SAP_Object_Def.works_sheet import works_sheet
from Login import *
from CONTROLLER_MDF_OBJECT_FIELD import CONTROLLER_MDF_OBJECT_FIELD

class TC_AUTOMATION_OBJECT_FIELD():
    Login()
    config = Config()
    ws = works_sheet('CDO_Field_Validate')
    def excute_process(self):
        data_list = self.ws.get_all_records()
        controller = CONTROLLER_MDF_OBJECT_FIELD()
        pending_data,process_data,id = controller.loaddata(data_list)
        self.config.red_url(driver, hw)
        durl = driver.current_url
        u = durl.split("=")[-2]
        for objectName in pending_data:
           self.process_Object(objectName,u,process_data)

    def process_Object(self,objectName,u,field_list):
        url = (
            f'https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=%s=1&t=GOObjectDefinition&i={objectName}')
        con_url = url % u
        driver.get(con_url)
        time.sleep(0.5)
        hw.ClickElement('//button[@aria-label="Take Action"]', 'xpath')
        time.sleep(0.3)
        hw.ClickElement('//a[@title="Make Correction"]', 'xpath')
        time.sleep(0.3)
        # field Items xpaths
        path = "//td[@class='field_label']/label[.='{0}']//parent::td//following-sibling::td//input"
        lipath = '(//li[@role="option"])[1]//a'
        sxpath = '(//td[@class="field_label"]/label[.="{0}"]//parent::td//following-sibling::td//span)[1]'
        satr = '//td//label[.="Hide Old Value"]//parent::td//following-sibling::td//input'
        lia = '//ul/li/a[.="{0}"]'
        # field Items xpaths end
        field_list = [obj for obj in field_list if obj.Object == objectName]
        for fieldName in field_list:
            field=hw.isElementPresent(f"//td//span[.='{fieldName.Name}']//parent::span//label[.='Name']//following-sibling::input",'xpath')
            if field == True:
                hw.ClickElement(
                    f'//td//span[.="{fieldName.Name}"]//parent::*//parent::*//parent::*//following-sibling::td//a[@class="writeComp fd-link fd-link--compact"]',
                    'xpath')
                hw.fill_field(path.format('Name'), 'xpath', keys=fieldName.Name)
                hw.fill_field(path.format('Maximum Length'), 'xpath', keys=fieldName.Maximum_Length)
                hw.dynamic_dropdown_click(path.format('Data Type'), 'xpath', value=fieldName.Data_Type, sendK=lipath)
                hw.static_dropdown_click(satr.format('Hide Old Value'), 'xpath', value=fieldName.Hide_Old_Value,
                                         iconclick=lia.format(fieldName.Hide_Old_Value), listel=sxpath.format('Hide Old Value'))
                hw.fill_field(path.format('Valid Values Source'), 'xpath', keys=fieldName.Valid_Values_Source)
                hw.fill_field(path.format('Decimal Precision'), 'xpath', keys=fieldName.Decimal_Precision)
                hw.static_dropdown_click(satr.format('Include Inactive Users'), 'xpath', value=fieldName.Include_Inactive_Users,
                                         iconclick=lia.format(fieldName.Include_Inactive_Users),
                                         listel=sxpath.format('Include Inactive Users'))
                hw.fill_field(path.format('UI Field Renderer'), 'xpath', keys=fieldName.UI_Field_Renderer)
                # transient
                hw.static_dropdown_click(satr.format('Transient'), 'xpath', value=fieldName.Transient,
                                         iconclick=lia.format(fieldName.Transient), listel=sxpath.format('Transient'))
                hw.fill_field(path.format('Help Text'), 'xpath', keys=fieldName.Help_Text)
                hw.static_dropdown_click(satr.format('Mask Value on UI'), 'xpath', value=fieldName.Mask_Value,
                                         iconclick=lia.format(fieldName.Mask_Value), listel=sxpath.format('Mask Value on UI'))
                hw.static_dropdown_click(satr.format('Show Trailing Zeros'), 'xpath', value=fieldName.Show_Trailing,
                                         iconclick=lia.format(fieldName.Show_Trailing),
                                         listel=sxpath.format('Show Trailing Zeros'))
                hw.fill_field(path.format('Default Value'), 'xpath', keys=fieldName.Default_Value)
                # Hide Seconds
                hw.static_dropdown_click(satr.format('Hide Seconds'), 'xpath', value=fieldName.Hide_Seconds,
                                         iconclick=lia.format(fieldName.Hide_Seconds), listel=sxpath.format('Hide Seconds'))
                # Required
                hw.static_dropdown_click(satr.format('Required'), 'xpath', value=fieldName.Required,
                                         iconclick=lia.format(fieldName.Required), listel=sxpath.format('Required'))
                # Visibility
                hw.static_dropdown_click(satr.format('Visibility'), 'xpath', value=fieldName.Visibility,
                                         iconclick=lia.format(fieldName.Visibility), listel=sxpath.format('Visibility'))
                # Status
                hw.static_dropdown_click(satr.format('Status'), 'xpath', value=fieldName.Status,
                                         iconclick=lia.format(fieldName.Status), listel=sxpath.format('Status'))

                # Label
                hw.fill_field(path.format('Label'), 'xpath', keys=fieldName.Label)
                # Cascade
                hw.static_dropdown_click(satr.format('Cascade'), 'xpath', value=fieldName.Cascade,
                                         iconclick=lia.format(fieldName.Cascade), listel=sxpath.format('Cascade'))
                # End Of Period
                hw.static_dropdown_click(satr.format('End Of Period'), 'xpath', value=fieldName.End_Period,
                                         iconclick=lia.format(fieldName.End_Period), listel=sxpath.format('End Of Period'))
                hw.ClickElement('//button[@title="Done"]', 'xpath')
            else:
                tr=hw.getElements("//span[.='Fields']//parent::div//following-sibling::div//table//tr",'xpath')
                size=len(tr)
                hw.ClickElement(f"((//span[.='Fields']//parent::div//following-sibling::div//table//tr)[{size}]//input[@class='formElement  fd-input fd-input--compact'])[1]",'xpath')
                time.sleep(0.2)
                hw.fill_field(f"((//span[.='Fields']//parent::div//following-sibling::div//table//tr)[{size}]//input[@class='formElement  fd-input fd-input--compact'])[1]",'xpath',keys="Lara")
                time.sleep(0.2)
        hw.ClickElement('//button[@name="Save"]', 'xpath')
        time.sleep(0.3)
        hw.popup('//div[@class="mdfErrorMsgList"]', 'xpath')
        time.sleep(0.3)

ob=TC_AUTOMATION_OBJECT_FIELD()
ob.excute_process()