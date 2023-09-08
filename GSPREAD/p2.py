import  gspread
from gspread_formatting import  *

# Google Sheet
sa =gspread.service_account()
sh =sa.open("Net2apps")
worksheet1=sh.get_worksheet(1)
# print(worksheet1)

# Formating Gspread

# fmt = CellFormat(
#     backgroundColor=Color(1, 0.9, 0.9),
#     textFormat=TextFormat(bold=True,foregroundColor=Color(1,0,1)),
#     horizontalAlignment='CENTER',
#     verticalAlignment='TOP'
#
#     )
# wh=CellFormat(
#     backgroundColor=Color(1, 0, 0.2)
# )
# cl2=CellFormat(
#     horizontalAlignment="CENTER",
#     textFormat=TextFormat(bold=True),
#     backgroundColor=Color(1,0.2,0.9)
#
# )
# format_cell_range(worksheet1, 'A1:A25', fmt)
# set_row_height(worksheet1, '1:100', 20)

