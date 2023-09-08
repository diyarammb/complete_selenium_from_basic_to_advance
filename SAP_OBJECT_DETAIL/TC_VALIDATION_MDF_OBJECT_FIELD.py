import time
from gspread_formatting import format_cell_ranges
from CONTROLLER_MDF_OBJECT_FIELD import CONTROLLER_MDF_OBJECT_FIELD
from Login import *
from Config_MDF_Object_Field import Config_MDF_Field
from SAP_OBJECT_DETAIL.Model_MDF_Object_Field import ValidProp
from SAP_Object_Def.works_sheet import works_sheet
class TC_VALIDATION_MDF_OBJECT_FIELD():
    Login()
    config=Config_MDF_Field()
    ws = works_sheet('CDO_Field_Validate')
    controller = CONTROLLER_MDF_OBJECT_FIELD()

    def excute_process(self):
        data_list = self.ws.get_all_records()
        pending_data,process_data,id = self.controller.loaddata(data_list)
        self.config.red_url(driver, hw)
        durl = driver.current_url
        u = durl.split("=")[-2]
        for objectName in pending_data:
            self.process_Object(objectName,u,process_data,id)


    def process_Object(self,objectName,u,field_list,id):
        url = (
            f'https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=%s=1&t=GOObjectDefinition&i={objectName}')
        con_url = url % u
        driver.get(con_url)
        time.sleep(0.5)
        # validations xpath start
        path = '//td[@class="field_label"]//label[.="{0}"]//parent::td//following-sibling::td//span[@class="readonly readComp"]'
        path2 = '(//td[@class="field_label"]//label[.="{0}"]//parent::td//following-sibling::td//span[@class="readonly read_only"])[1]'
        #     # element check
        field_list = [obj for obj in field_list if obj.Object == objectName]
        for fieldName in field_list:
            hw.ClickElement(
                f'//td//span[.="{fieldName.Name}"]//parent::*//parent::*//parent::*//following-sibling::td//a[@class="readComp fd-link fd-link--compact"]',
                'xpath')
            Name = hw.GetElementText(path.format('Name'), 'xpath')
            Database = hw.GetElementText(path2.format('Database Field Name'), 'xpath')
            Maximum_Length = hw.GetElementText(path.format('Maximum Length'), 'xpath')
            Data_Type = hw.GetElementText(path.format('Data Type'), 'xpath')
            Valid_Values_Source = hw.GetElementText(path.format('Valid Values Source'), 'xpath')
            Hide_Old_Value = hw.GetElementText(path.format('Hide Old Value'), 'xpath')
            Decimal_Precision = hw.GetElementText(path.format('Decimal Precision'), 'xpath')
            Include_Inactive_Users = hw.GetElementText(path.format('Include Inactive Users'), 'xpath')
            UI_Field_Renderer = hw.GetElementText(path.format('UI Field Renderer'), 'xpath')
            Transient = hw.GetElementText(path.format('Transient'), 'xpath')
            Help_Text = hw.GetElementText(path.format('Help Text'), 'xpath')
            Mask_Value = hw.GetElementText(path.format('Mask Value on UI'), 'xpath')
            Show_Trailing = hw.GetElementText(path.format('Show Trailing Zeros'), 'xpath')
            Default_Value = hw.GetElementText(path.format('Default Value'), 'xpath')
            Hide_Seconds = hw.GetElementText(path.format('Hide Seconds'), 'xpath')
            Required = hw.GetElementText(path.format('Required'), 'xpath')
            Visibility = hw.GetElementText(path.format('Visibility'), 'xpath')
            Status = hw.GetElementText(path.format('Status'), 'xpath')
            Label = hw.GetElementText(path.format('Label'), 'xpath')
            Cascade = hw.GetElementText(path.format('Cascade'), 'xpath')
            Inactivated_By = hw.GetElementText(path2.format('Inactivated By'), 'xpath')
            End_Period = hw.GetElementText(path2.format('End Of Period'), 'xpath')
            #     # validations cell Name
            col=ValidProp()
            red = self.config.cell_red
            green = self.config.cell_green
            col_list = []
            if Name==False:
                col_list.append((f'{col.Name + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.Name + str(fieldName.id + 1)}', green))
            if Database == False:
                col_list.append((f'{col.Database + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.Database + str(fieldName.id + 1)}', green))
            if Maximum_Length == False:
                col_list.append((f'{col.Maximum_Length + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.Maximum_Length + str(fieldName.id + 1)}', green))
                # Data_Type
            if Data_Type == False:
                col_list.append((f'{col.Data_Type + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.Data_Type + str(fieldName.id + 1)}', green))
            # Valid_Values_Source

            if Valid_Values_Source == False:
                col_list.append((f'{col.Valid_Values_Source + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.Valid_Values_Source + str(fieldName.id + 1)}', green))
            # Hide_Old_Value
            if Hide_Old_Value == False:
                col_list.append((f'{col.Hide_Old_Value + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.Hide_Old_Value + str(fieldName.id + 1)}', green))

            if Decimal_Precision == False:
                col_list.append((f'{col.Decimal_Precision + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.Decimal_Precision + str(fieldName.id + 1)}', green))
            # Include_Inactive_Users
            if Include_Inactive_Users == False:
                col_list.append((f'{col.Include_Inactive_Users + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.Include_Inactive_Users + str(fieldName.id + 1)}', green))
                # UI_Field_Renderer

            if UI_Field_Renderer == False:
                col_list.append((f'{col.UI_Field_Renderer + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.UI_Field_Renderer + str(fieldName.id + 1)}', green))
            # Transient
            if Transient == False:
                col_list.append((f'{col.Transient + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.Transient + str(fieldName.id + 1)}', green))
                # Help_Text
            if Help_Text == False:
                col_list.append((f'{col.Help_Text + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.Help_Text + str(fieldName.id + 1)}', green))
                # Mask_Value
            if Mask_Value == False:
                col_list.append((f'{col.Mask_Value + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.Mask_Value + str(fieldName.id + 1)}', green))
                # Show_Trailing
            if Show_Trailing == False:
                col_list.append((f'{col.Show_Trailing + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.Show_Trailing + str(fieldName.id + 1)}', green))
            # Default_Value
            if Default_Value == False:
                col_list.append((f'{col.Default_Value + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.Default_Value + str(fieldName.id + 1)}', green))
            # Hide_Seconds
            if Hide_Seconds == False:
                col_list.append((f'{col.Hide_Seconds + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.Hide_Seconds + str(fieldName.id + 1)}', green))
                # Required

            if Required == False:
                col_list.append((f'{col.Required + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.Required + str(fieldName.id + 1)}', green))
                # Visibility
            if Visibility == False:
                col_list.append((f'{col.Visibility + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.Visibility + str(fieldName.id + 1)}', green))
                # Status

            if Status == False:
                col_list.append((f'{col.Status + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.Status + str(fieldName.id + 1)}', green))
                # Label
            if Label == False:
                col_list.append((f'{col.Label + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.Label + str(fieldName.id + 1)}', green))
                # Cascade
            if Cascade == False:
                col_list.append((f'{col.Cascade + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.Cascade + str(fieldName.id + 1)}', green))
                # Inactivated_By
            if Inactivated_By == False:
                col_list.append((f'{col.Inactivated_By + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.Inactivated_By + str(fieldName.id + 1)}', green))

            # End_Period
            if End_Period == False:
                col_list.append((f'{col.End_Period + str(fieldName.id + 1)}', red))
            else:
                col_list.append((f'{col.End_Period + str(fieldName.id + 1)}', green))
                # Object
            if End_Period == False:
                    col_list.append((f'{col.Object + str(fieldName.id + 1)}', red))
            else:
                    col_list.append((f'{col.Object + str(fieldName.id + 1)}', green))

            # formate cells
            format_cell_ranges(self.ws, col_list)
             # validations xpath end
            #
            hw.ClickElement('//button[@title="Done"]', 'xpath')
            time.sleep(0.2)
        self.controller.fill_worksheet_Processing_section(self.ws,id)


ob=TC_VALIDATION_MDF_OBJECT_FIELD()
ob.excute_process()