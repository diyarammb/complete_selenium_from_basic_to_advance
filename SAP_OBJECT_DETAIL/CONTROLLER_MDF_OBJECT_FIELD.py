from gspread import Cell
from Model_MDF_Object_Field import *
from SAP_Object_Def.works_sheet import works_sheet


class CONTROLLER_MDF_OBJECT_FIELD():

    def fillworksheet(self,ws,datalist,row):
            cell_list=[]
            for data in datalist:
                cell_list.append(Cell(row=row,col=1,value=row-1))
                cell_list.append(Cell(row=row,col=2,value=data.Object))
                cell_list.append(Cell(row=row,col=3,value=data.Name))
                cell_list.append(Cell(row=row,col=4,value=data.Database))
                cell_list.append(Cell(row=row,col=5,value=data.Maximum_Length))
                cell_list.append(Cell(row=row,col=6,value=data.Data_Type))
                cell_list.append(Cell(row=row,col=7,value=data.Valid_Values_Source))
                cell_list.append(Cell(row=row,col=8,value=data.Hide_Old_Value))
                cell_list.append(Cell(row=row,col=9,value=data.Decimal_Precision))
                cell_list.append(Cell(row=row,col=10,value=data.Include_Inactive_Users))
                cell_list.append(Cell(row=row,col=11,value=data.UI_Field_Renderer))
                cell_list.append(Cell(row=row,col=12,value=data.Transient))
                cell_list.append(Cell(row=row,col=13,value=data.Help_Text))
                cell_list.append(Cell(row=row,col=14,value=data.Mask_Value))
                cell_list.append(Cell(row=row,col=15,value=data.Show_Trailing))
                cell_list.append(Cell(row=row,col=16,value=data.Default_Value))
                cell_list.append(Cell(row=row,col=17,value=data.Hide_Seconds))
                cell_list.append(Cell(row=row,col=18,value=data.Required))
                cell_list.append(Cell(row=row,col=19,value=data.Visibility))
                cell_list.append(Cell(row=row,col=20,value=data.Status))
                cell_list.append(Cell(row=row,col=21,value=data.Label))
                cell_list.append(Cell(row=row,col=22,value=data.Cascade))
                cell_list.append(Cell(row=row,col=23,value=data.Inactivated_By))
                cell_list.append(Cell(row=row,col=24,value=data.End_Period))
                row + 1
            ws.update_cells(cell_list)
    # loadsheet data
    def loaddata(self,data_list):
        pending_data = []
        processList = []
        for i in data_list:
            model=Model_Details_Field()
            model.id=i['ID']
            model.Object=i['Object']
            model.Name=i['Name']
            model.Database=i['Database']
            model.Maximum_Length=i['Maximum_Length']
            model.Data_Type=i['Data_Type']
            model.Data_Type=i['Valid_Values_Source']
            model.Hide_Old_Value=i['Hide_Old_Value']
            model.Decimal_Precision=i['Decimal_Precision']
            model.Include_Inactive_Users=i['Include_Inactive_Users']
            model.UI_Field_Renderer=i['UI_Field_Renderer']
            model.Transient=i['Transient']
            model.Help_Text=i['Help_Text']
            model.Mask_Value=i['Mask_Value']
            model.Show_Trailing=i['Show_Trailing']
            model.Default_Value=i['Default_Value']
            model.Hide_Seconds=i['Hide_Seconds']
            model.Required=i['Required']
            model.Visibility=i['Visibility']
            model.Status=i['Status']
            model.Label=i['Label']
            model.Cascade=i['Cascade']
            model.Inactivated_By=i['Inactivated_By']
            model.End_Period=i['End_Period']
            # pending model
            pending_data.append(model)
            # process model
            process_model=Process_Model_Field()
            process_model.Heading=i['Code']
            process_model.pid=i['ID']
            process_model.Status_details=i['Status_details']
            processList.append(process_model)
        pending_element=[ob.Heading for ob in processList if ob.Status_details =="Pending"]
        id=[ob.pid for ob in processList if ob.Status_details =="Pending"]
        process_elements=[ob for ob in pending_data if ob.Object in pending_element]
        return pending_element,process_elements,id

    def fill_worksheet_Processing_section(self,ws,id):
        for pid in id:
            ws.update_acell(f'AA{pid + 1}', 'Processed')





