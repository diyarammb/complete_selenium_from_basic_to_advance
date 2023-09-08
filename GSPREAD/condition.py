from gspread_formatting import *
import  gspread
sa =gspread.service_account()
sh=sa.open("Net2apps")
ws=sh.get_worksheet(3)

# val = ws.acell('G2').value
# print(val)
# ValidationRule=DataValidationRule(
#     BooleanCondition('ONE_OF_LIST', ['Pending', 'Processed']),
#     showCustomUi=True
# )
# set_data_validation_for_cell_range(ws ,'G2:G50',  ValidationRule)

fmt = CellFormat(
    backgroundColor=Color(0, 1, 0),
    textFormat=TextFormat(bold=True, foregroundColor=Color(0, 0, 0)),
    horizontalAlignment='LEFT'
    )
dng = CellFormat(
    backgroundColor=Color(1, 0, 0),
    textFormat=TextFormat(bold=True, foregroundColor=Color(0, 0, 0)),
)

for i in range(2,6):
    val = ws.acell(f'G{i}').value

    if val == "pending":
        ws.update_cells(2,7,"Procced")

        # Your existing code for scraping data goes here...

        # Construct the data to be inserted into the Google Sheet
        data = []
        for i in range(len(Heading)):
            row_data = [Heading[i], Score[i], Score_lable[i], Score_desc[i]]
            data.append(row_data)

        # Set up the gspread client (replace 'your_credentials.json' with your actual credentials file)
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('your_credentials.json', scope)
        client = gspread.authorize(credentials)

        # Replace 'Your Google Sheet Name' with the name of your Google Sheet
        sheet_name = 'Your Google Sheet Name'
        sheet = client.open(sheet_name).sheet1

        # Insert the data into the Google Sheet
        # Starting from row 2, since row 1 might contain headers
        sheet.insert_rows(data, row=2)

        # Continue with the rest of your code...



