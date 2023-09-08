import time
from Controller_MDF_Object import Controller_Object
from Model_MDF_Object import Validations_Props
from works_sheet import works_sheet
from Login import *
from Config_MDF_Object import Config
from gspread_formatting import  *


class TC_VALIDATE_MDF_Object():
    Login()
    config = Config()
    ws = works_sheet('Validate-CDO')

    def excute_process(self):
        data_list=self.ws.get_all_records()
        controller=Controller_Object()
        pending_data=controller.Load_data(data_list)
        self.config.red_url(driver,hw)
        durl = driver.current_url
        u = durl.split("=")[-2]
        for i in pending_data:
            self.object_process(i,u)

    def object_process(self,data,u):
            url = (
                f'https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=%s=1&t=GOObjectDefinition&i={data.code}')
            con_url = url % u
            driver.get(con_url)
            time.sleep(1)
            col=Validations_Props()
            code=hw.isElementPresent(f"(//table/tbody//td//span//span[.='{data.code}'])[1]","xpath")
            Effective=hw.isElementPresent(f"(//table/tbody//td//span//span[.='{data.Effective}'])[1]","xpath")
            Visibility=hw.isElementPresent(f"(//table/tbody//td//span//span[.='{data.Visibility}'])[1]","xpath")
            Status=hw.isElementPresent(f"(//table/tbody//td//span//span[.='{data.Status}'])[1]","xpath")
            History=hw.isElementPresent(f"(//table/tbody//td//span//span[.='{data.History}'])[1]","xpath")
            Screen=hw.isElementPresent(f"(//table/tbody//td//span//span[.='{data.Screen}'])[1]","xpath")
            Label=hw.isElementPresent(f"(//table/tbody//td//span//span[.='{data.Label}'])[1]","xpath")
            Description=hw.isElementPresent(f"(//table/tbody//td//span//span[.='{data.Description}'])[1]","xpath")
            Version=hw.isElementPresent(f"(//table/tbody//td//span//span[.='{data.Version}'])[1]","xpath")
            Subject=hw.isElementPresent(f"(//table/tbody//td//span//span[.='{data.Subject}'])[1]","xpath")
            Workflow=hw.isElementPresent(f"(//table/tbody//td//span//span[.='{data.Workflow}'])[1]","xpath")
            Pending=hw.isElementPresent(f"(//table/tbody//td//span//span[.='{data.Pending}'])[1]","xpath")
            Todo=hw.isElementPresent(f"(//table/tbody//td//span//span[.='{data.Todo}'])[1]","xpath")
            Object=hw.isElementPresent(f"(//table/tbody//td//span//span[.='{data.Object}'])[1]","xpath")
            Secured=hw.isElementPresent(f"(//table/tbody//td//span//span[.='{data.Secured}'])[1]","xpath")
            Permission=hw.isElementPresent(f"(//table/tbody//td//span//span[.='{data.Permission}'])[1]","xpath")
            RBP=hw.isElementPresent(f"(//table/tbody//td//span//span[.='{data.RBP}'])[1]","xpath")
            Criteria=hw.isElementPresent(f"(//table/tbody//td//span//span[.='{data.Criteria}'])[1]","xpath")
            Blocking=hw.isElementPresent(f"(//table/tbody//td//span//span[.='{data.Blocking}'])[1]","xpath")
            red = self.config.cell_red
            green = self.config.cell_green
            col_list=[]
            if code ==False:
                col_list.append((f'{col.code+str(data.id+1)}',red))
            else:
                col_list.append((f'{col.code+str(data.id+1)}',green))
            # Effective
            if Effective ==False:
                col_list.append((f'{col.Effective+str(data.id+1)}',red))
            else:
                 col_list.append((f'{col.Effective+str(data.id+1)}',green))
                # Visibility
            if Visibility ==False:
                 col_list.append((f'{col.Visibility+str(data.id+1)}',red))
            else:
                 col_list.append((f'{col.Visibility+str(data.id+1)}',green))
                # Status
            if Status ==False:
                 col_list.append((f'{col.Status+str(data.id+1)}',red))
            else:
                 col_list.append((f'{col.Status+str(data.id+1)}',green))
                # History
            if History ==False:
                 col_list.append((f'{col.History+str(data.id+1)}',red))
            else:
                 col_list.append((f'{col.History+str(data.id+1)}',green))
                # Screen
            if Screen ==False:
                 col_list.append((f'{col.Screen+str(data.id+1)}',red))
            else:
                 col_list.append((f'{col.Screen+str(data.id+1)}',green))
                # Label
            if Label ==False:
                 col_list.append((f'{col.Label+str(data.id+1)}',red))
            else:
                 col_list.append((f'{col.Label+str(data.id+1)}',green))
            # Description
            if Description ==False:
                 col_list.append((f'{col.Description+str(data.id+1)}',red))
            else:
                 col_list.append((f'{col.Description+str(data.id+1)}',green))
                # Version
            if Version ==False:
                 col_list.append((f'{col.Version+str(data.id+1)}',red))
            else:
                 col_list.append((f'{col.Version+str(data.id+1)}',green))
                # Subject
            if Subject ==False:
                 col_list.append((f'{col.Subject+str(data.id+1)}',red))
            else:
                 col_list.append((f'{col.Subject+str(data.id+1)}',green))
                # Workflow
            if Workflow ==False:
                 col_list.append((f'{col.Workflow+str(data.id+1)}',red))
            else:
                 col_list.append((f'{col.Workflow+str(data.id+1)}',green))
                # Pending
            if Pending ==False:
                 col_list.append((f'{col.Pending+str(data.id+1)}',red))
            else:
                 col_list.append((f'{col.Pending+str(data.id+1)}',green))
                # Todo
            if Todo ==False:
                 col_list.append((f'{col.Todo+str(data.id+1)}',red))
                # Object
            else:
                 col_list.append((f'{col.Todo+str(data.id+1)}',green))
            if Object ==False:
                 col_list.append((f'{col.Object+str(data.id+1)}',red))
            else:
                 col_list.append((f'{col.Object+str(data.id+1)}',green))
            if Secured == False:
                col_list.append((f'{col.Secured + str(data.id + 1)}', red))
            else:
                col_list.append((f'{col.Secured + str(data.id + 1)}', green))
            if Permission == False:
                col_list.append((f'{col.Permission + str(data.id + 1)}', red))
            else:
                col_list.append((f'{col.Permission + str(data.id + 1)}', green))
            if RBP == False:
                col_list.append((f'{col.RBP + str(data.id + 1)}', red))
            else:
                col_list.append((f'{col.RBP + str(data.id + 1)}', green))
            if Criteria == False:
                col_list.append((f'{col.Criteria + str(data.id + 1)}', red))
            else:
                col_list.append((f'{col.Criteria + str(data.id + 1)}', green))
            if Blocking == False:
                col_list.append((f'{col.Blocking + str(data.id + 1)}', red))
            else:
                col_list.append((f'{col.Blocking + str(data.id + 1)}', green))

            format_cell_ranges(self.ws,col_list)
            self.ws.update_acell(f'U{data.id+ 1}', 'Processed')


ob= TC_VALIDATE_MDF_Object()
ob.excute_process()


