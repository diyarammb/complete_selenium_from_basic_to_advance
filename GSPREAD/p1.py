import gspread

sa =gspread.service_account()

sh=sa.open('Net2apps')
# sh1=sa.create("19MTE")
#share gsheet throuhg Gmail
# sh.share('dayakarma48@gmail.com', perm_type='user', role='writer')
# get worksheet by index
worksheet = sh.get_worksheet(1)
# print(worksheet)
# create worksheet
# worksheet = sh.add_worksheet(title="19MTE", rows=100, cols=20)
# print(worksheet)

# sh=sa.open("19MTE")
# worksheet = sh.get_worksheet(1)
# std=worksheet.get_all_values()
# for i in std:
#     print(i)

# Sheet Formating

# worksheet.update_title("19MTE")
# worksheet.update_tab_color({"red": 1, "green": 0.5, "blue": 0.5})
# name=worksheet.acell('A24')
# rows=worksheet.row_values(1)
# print(rows)
# name=worksheet.col_values(1)
# for i in name:
#     print(i)
# # print(name)
# find value from cels
# cell = worksheet.find("dayaram")
# cell_list = worksheet.findall("awais")
# print(str(len(cell_list)))

#
# print("Found something at R%sC%s" % (cell.row, cell.col))

# update cell values
# row=input("Enter Row Num")
# name=input("Enter Name")
# worksheet.update_cell(int(row),1,name)
# for i in range (7,22):
#     row = input("Enter Row Num")
#     name = input("Enter Name")
#     worksheet.update_cell(int(row), 1, name)
# enter the value using looop in gshheet
# for i in range (11,26):
#     gpa=input(f"{i}Enter GPA")
#     worksheet.update_cell(i, 3, float(gpa))

# print("============Records=================")
# records=worksheet.get_all_records()
# print(records)
# print("============Values=================")
# values=worksheet.get_all_values()
# print(values)

# user=["Sardar Bheel","19MTE11",2.6]
# insert data
# worksheet.insert_row(user,28)
# append data
# worksheet.append_row(user)
# delete rows
# worksheet.delete_row(27)
print()