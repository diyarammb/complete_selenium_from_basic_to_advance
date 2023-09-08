# import time
# import gspread
# from gspread_formatting import *
# from Emad_Task_4 import Task4
#
# sa = gspread.service_account()
# sh = sa.open("Gspread")
# ws = sh.worksheet("Tasks")
#
# valid_element_format = CellFormat(backgroundColor=Color(0, 1, 0))
# invalid_element_format = CellFormat(backgroundColor=Color(1, 0, 0))
#
# sheet_data = ws.get_all_values()
# col_G_values = ws.col_values(7)
#
# for index, value in enumerate(col_G_values):
#     if value == 'Pending':
#         heading_val = ws.get(f'F{index + 1}')[0][0]
#         try:
#             ind = [row[0] for row in sheet_data].index(heading_val) + 1
#         except ValueError:
#             continue
#
#         for n, data in enumerate(sheet_data[ind - 1:], 1):
#             x1, x2, x3, x4, _, _, _ = data
#
#             try:
#                 atr_list = x4.split('https://www.w3schools.com')
#                 string_atr = ''.join(atr_list)
#             except:
#                 string_atr = x4
#
#             heading_check = Task4.wrap.getElement(f"//h5[.='{x2}']", "xpath")
#             sub_heading_check = Task4.wrap.getElement(f"//h5[.='{x2}']//parent::*//parent::div//a[.='{x3}']", "xpath")
#             link_check = Task4.wrap.getElement(f"//h5[.='{x2}']//parent::*//parent::div//a[@href='{string_atr}']", "xpath")
#
#             if heading_check:
#                 format_cell_range(ws, f'B{ind + n}', valid_element_format)
#             else:
#                 format_cell_range(ws, f'B{ind + n}', invalid_element_format)
#
#             if sub_heading_check:
#                 format_cell_range(ws, f'C{ind + n}', valid_element_format)
#             else:
#                 format_cell_range(ws, f'C{ind + n}', invalid_element_format)
#
#             if link_check:
#                 format_cell_range(ws, f'D{ind + n}', valid_element_format)
#             else:
#                 format_cell_range(ws, f'D{ind + n}', invalid_element_format)
#
#             time.sleep(1)
#
#         col_G_values[index] = 'Processed'
#         ws.update(f'G{index + 1}', 'Processed')
# # Assuming the "approved" status is present in column G (index 6)
# status_col_index = 6
#
# for id, i in enumerate(HeadingOfElement):
#     subHeading = self.hw.GetElementlistofText(
#         f"//div[@class='w3-row w3-center w3-small']//*[.='{i}']/following-sibling::a",
#         "xpath")
#
#     for j in subHeading:
#         s = self.hw.getElement(f"//a[.='{j}']", "xpath")
#         l = s.get_attribute("href")
#
#         # Assuming you want to set the background color of the cell in column E (index 4)
#         # You can change this index if necessary
#         col_index = 4
#
#         if l:
#             # Data is available in the cell, check the status in column G
#             status_cell_value = self.ws.cell(id + 2, status_col_index).value
#
#             if status_cell_value.lower() == "approved":
#                 # Status is "approved", set the background color to green
#                 cell_list_to_format.append((id + 2, col_index + 1, CellFormat(backgroundColor=Color(0, 1, 0))))
#             else:
#                 # Status is not "approved", set the background color to red
#                 cell_list_to_format.append((id + 2, col_index + 1, CellFormat(backgroundColor=Color(1, 0, 0))))
#         else:
#             # Data is not available, set the background color to default (white)
#             cell_list_to_format.append((id + 2, col_index + 1, CellFormat(backgroundColor=Color(1, 1, 1))))
#         time.sleep(1)
import time
import gspread
from gspread_formatting import *
from selenium import webdriver
from Task.Handy import Handy

class Task3():
    # Your other code here...

    def DataValidation(self):
        sa = gspread.service_account()
        sh = sa.open("Net2apps")
        ws = sh.get_worksheet(0)  # Assuming the data is in the first worksheet (index 0)

        # Get all values in the SubHeadingLink column (column C, index 2)
        subheading_links = ws.col_values(3)[1:]  # Skip the header row

        # List to store cell formatting settings
        cell_list_to_format = []

        # Open a Chrome webdriver
        baseurl = "https://www.w3schools.com/python/default.asp"
        driver = webdriver.Chrome()
        driver.maximize_window()
        hw = Handy(driver)
        driver.get(baseurl)
        driver.implicitly_wait(4)

        for id, link in enumerate(subheading_links):
            if link.strip():  # Check if the link is not empty
                # Data is available in the cell, set the background color of the corresponding "Status" cell to green
                # Assuming the "Status" column (column E, index 4) corresponds to the "SubHeadingLink" column (column C, index 2)
                # You can change the column indices if necessary
                col_index_subheading_link = 2
                col_index_status = 4

                # Get the corresponding "Status" cell
                status_cell = ws.cell(id + 2, col_index_status + 1)

                # Check if the link is valid using your Handy class or any other method to validate links
                # Replace this part with your own logic to validate links
                is_valid_link = hw.ValidateLink(link)

                if is_valid_link:
                    # If the link is valid, set the background color of the "Status" cell to green
                    cell_list_to_format.append((status_cell.row, status_cell.col, CellFormat(backgroundColor=Color(0, 1, 0))))
                else:
                    # If the link is not valid, set the background color of the "Status" cell to default (white)
                    cell_list_to_format.append((status_cell.row, status_cell.col, CellFormat(backgroundColor=Color(1, 1, 1))))

        format_cell_ranges(ws, cell_list_to_format)
        driver.quit()  # Close the Chrome webdriver

# Create an instance of Task3 and call the DataValidation method
ob = Task3()
ob.DataValidation()
