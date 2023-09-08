from gspread import Cell
from Model_MDF_Object import *
class Controller_Object():
    def fill_worksheet(self,ws,obj_list,row):
        cell_list=[]
        for e in obj_list:
            cell_list.append(Cell(row=row,col=1,value=row-1))
            cell_list.append(Cell(row=row,col=2,value=e.code))
            cell_list.append(Cell(row=row,col=3,value=e.Effective))
            cell_list.append(Cell(row=row,col=4,value=e.Visibility))
            cell_list.append(Cell(row=row,col=5,value=e.Status))
            cell_list.append(Cell(row=row,col=6,value=e.History))
            cell_list.append(Cell(row=row,col=7,value=e.Screen))
            cell_list.append(Cell(row=row,col=8,value=e.Label))
            cell_list.append(Cell(row=row,col=9,value=e.Description))
            cell_list.append(Cell(row=row,col=10,value=e.Version))
            cell_list.append(Cell(row=row,col=11,value=e.Subject))
            cell_list.append(Cell(row=row,col=12,value=e.Workflow))
            cell_list.append(Cell(row=row,col=13,value=e.Pending))
            cell_list.append(Cell(row=row,col=14,value=e.Todo))
            cell_list.append(Cell(row=row,col=15,value=e.Object))
            cell_list.append(Cell(row=row,col=16,value=e.Secured))
            cell_list.append(Cell(row=row,col=17,value=e.Permission))
            cell_list.append(Cell(row=row,col=18,value=e.RBP))
            cell_list.append(Cell(row=row,col=19,value=e.Criteria))
            cell_list.append(Cell(row=row,col=20,value=e.Blocking))
            row + 1
        ws.update_cells(cell_list)

    def Load_data(self, data_list):
        pending_data = []
        processList = []
        for data in data_list:
            model_config = Model_Object()
            model_config.id = data['id']
            model_config.code = data['Code']
            model_config.Label = data['Label']
            model_config.Description = data['Description']
            model_config.Effective = data['Effective']
            model_config.History = data['MDF Version History']
            model_config.Object = data['Object Category']
            model_config.Screen = data['Default Screen']
            model_config.Pending = data['Pending Data']
            model_config.Subject = data['Subject User Field']
            model_config.Status = data['Status']
            model_config.Todo = data['Todo Category']
            model_config.Version = data['API Sub Version']
            model_config.Workflow = data['Workflow Routing']
            model_config.Visibility = data['API Visibility']
            model_config.Visibility = data['Secured']
            model_config.Visibility = data['Permission']
            model_config.Visibility = data['RBP']
            model_config.Visibility = data['Criteria']
            model_config.Visibility = data['Blocking']
            # all data appends
            pending_data.append(model_config)
            # pending data list
            p = Process_Object()
            p.Heading = data['Code']
            p.Status_sap = data['SF_Status']
            processList.append(p)
        pending_elements = [obj.Heading for obj in processList if obj.Status_sap == "Pending"]
        process_elements=[obj for obj in pending_data if obj.code in pending_elements]
        return process_elements

