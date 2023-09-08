# rurl="https://pmsalesdemo8.successfactors.com/acme?fbacme_o=admin&pess_old_admin=true&ap_param_action=form_rating_scale&itrModule=talent&_s.crb=%s"
# d="23425"
# url =rurl%d
# print(url)
# # lst = {'=Woman','=Men'}
# # url_test = 'http://www.Holiday.com/%s/Beach'
# # for i in lst:
# #      url = url_test %i
# #      print (url)
#
# # Assume the data should be written starting from cell A1.
# cell_list = worksheet.range('A1:C4')
#
# # Flatten the three lists into one list.
# data_to_insert = list1 + list2 + list3
#
# # Fill the cell_list with the data from the combined list.
# for cell, data in zip(cell_list, data_to_insert):
#     cell.value = data
#
# # Update the worksheet with the new data.
# worksheet.update_cells(cell_list)
#
# link = self.hw.getElement(f"//a[.='{v}']", "xpath")
# for c, i in enumerate(Heading):
#     c += 3
#     if i == v:
#         format_cell_range(ws, f'B{c}', fmt1)
#     else:
#         format_cell_range(ws, f'B{c}', fmt)
#
#     if v == "Performance Rating Scale" or v == 'Default Scale':
#         link.click()
#         time.sleep(2)
#         self.hw.getElement("//button[@name='OK']", "xpath").click()
#         time.sleep(2)
#         self.hw.getElement("//span[@class=' icon icon_cancel']", "xpath").click()
#         time.sleep(1)
#     else:
#         link.click()
#         time.sleep(4)
#         # self.driver.implicitly_wait(10)
#         score = self.hw.GetElementlistofattributeText(
#             "//div[@class='gridCell']//span[@title='The numerical value used for rating calculations, for example 3.0.']//input[@type='text']",
#             'xpath', 'value')
#         label = self.hw.GetElementlistofattributeText(
#             "//div[@class='gridCell']//span[@title='The short title or abbreviation of the rating increment. For example, Meets Expectations.']//input[@type='text']",
#             'xpath', 'value')
#         desc = self.hw.GetElementlistofText(
#             "//div[@class='gridCell']//span[@title='The description of the rating increment. This is helpful to explain to your users how to use the rating.']/textarea",
#             'xpath')
#         sd = self.hw.GetElementText("//span[@class='ratingScaleTextArea']//textarea", "xpath")
#         for r, s in enumerate(score):
#             if s is not None:
#                 format_cell_range(ws, f'D{c}', fmt1)
#             else:
#                 format_cell_range(ws, f'D{c}', fmt)
#         time.sleep(1)
#         self.hw.getElement("//span[@class=' icon icon_cancel']", "xpath").click()
#         time.sleep(1)
#
#         import time
#         from gspread_formatting import *
#         from task2 import SafScrape
#         import gspread
#
#
#         class Validation():
#             login = SafScrape()
#             login.LoginSap()
#
#             def Validate(self):
#                 sa = gspread.service_account()
#                 sh = sa.open('Net2apps')
#                 ws = sh.get_worksheet(5)
#                 red = CellFormat(
#                     backgroundColor=Color(1, 0, 0), )
#                 green = CellFormat(
#                     backgroundColor=Color(0, 1, 0))
#                 status = ws.col_values(9)[1:]
#                 Heading = ws.col_values(2)[1:]
#                 title = ws.col_values(8)[1:]
#                 for si, s in enumerate(status):
#                     if s == "Pending":
#                         v = title[si]
#                         for c, i in enumerate(Heading):
#                             c += 2
#                             link = self.hw.getElement(f"//a[.='{v}']", "xpath")
#                             # if i == v:
#                             if v == "Performance Rating Scale" or v == 'Default Scale':
#                                 link.click()
#                                 time.sleep(2)
#                                 self.hw.getElement("//button[@name='OK']", "xpath").click()
#                                 time.sleep(2)
#                                 self.hw.getElement("//span[@class=' icon icon_cancel']", "xpath").click()
#                                 time.sleep(1)
#                             else:
#                                 link.click()
#                                 time.sleep(3)
#                                 score = self.hw.GetElementlistofattributeText(
#                                     "//div[@class='gridCell']//span[@title='The numerical value used for rating calculations, for example 3.0.']//input[@type='text']",
#                                     'xpath', 'value')
#                                 label = self.hw.GetElementlistofattributeText(
#                                     "//div[@class='gridCell']//span[@title='The short title or abbreviation of the rating increment. For example, Meets Expectations.']//input[@type='text']",
#                                     'xpath', 'value')
#                                 desc = self.hw.GetElementlistofText(
#                                     "//div[@class='gridCell']//span[@title='The description of the rating increment. This is helpful to explain to your users how to use the rating.']/textarea",
#                                     'xpath')
#                                 sd = self.hw.GetElementText("//span[@class='ratingScaleTextArea']//textarea", "xpath")
#                                 for r, s in enumerate(score):
#                                     print(s, ' ', label[r], ' ', desc[r])
#
#                             time.sleep(1)
#                             self.hw.getElement("//span[@class=' icon icon_cancel']", "xpath").click()
#                             time.sleep(1)
#                         # status[si] = 'Processed'
#                         # ws.update_acell(f'I{si}', 'Processed')
#
#
#         ob = Validation()
#         ob.Validate()
#         import time
#         import gspread
#         from task2 import SafScrape
#
#
#         class AutomatedSap():
#             def sheet_automat(self):
#                 login = SafScrape()
#                 login.LoginSap()
#                 sa = gspread.service_account()
#                 sh = sa.open('Net2apps')
#                 ws = sh.get_worksheet(6)
#                 values = ws.get_all_records()
#                 status = ws.col_values(9)[1:]
#                 title = ws.col_values(8)[1:]
#                 for i, s in enumerate(status):
#                     if s == "Pending":
#                         v = title[i]
#                         link = login.hw.getElement(f"//a[.='{v}']", "xpath")
#                         link.click()
#                         time.sleep(2)
#                         try:
#                             login.hw.getElement("//button[@name='OK']", "xpath").click()
#                             time.sleep(2)
#                         except:
#                             print("No Ok")
#                         time.sleep(4)
#                         score = login.hw.GetElementlistofattributeText(
#                             "//div[@class='gridCell']//span[@title='The numerical value used for rating calculations, for example 3.0.']//input[@type='text']",
#                             'xpath', 'value')
#                         label = login.hw.GetElementlistofattributeText(
#                             "//div[@class='gridCell']//span[@title='The short title or abbreviation of the rating increment. For example, Meets Expectations.']//input[@type='text']",
#                             'xpath', 'value')
#                         desc = login.hw.GetElementlistofText(
#                             "//div[@class='gridCell']//span[@title='The description of the rating increment. This is helpful to explain to your users how to use the rating.']/textarea",
#                             'xpath')
#                         sd = login.hw.GetElementText("//span[@class='ratingScaleTextArea']//textarea", "xpath")
#                         for j in values:
#                             if j['Scale Name'] == v:
#                                 for index, s in enumerate(score):
#                                     print(j)
#
#                         time.sleep(1)
#                         login.hw.getElement("//span[@class=' icon icon_cancel']", "xpath").click()
#                         time.sleep(2)
#
#
#         ob = AutomatedSap()
#         ob.sheet_automat()
# import time
# import  gspread
# from gspread_formatting import  *
# from task2 import SafScrape
# class AutomatedSap():
#     def sheet_automat(self):
#         login = SafScrape()
#         login.LoginSap()
#         red = CellFormat(
#             backgroundColor=Color(1, 0, 0), )
#         green = CellFormat(
#             backgroundColor=Color(0, 1, 0))
#         sa = gspread.service_account()
#         sh = sa.open('Net2apps')
#         ws = sh.get_worksheet(6)
#         values = ws.get_all_records()
#         status=ws.col_values(9)[1:]
#         title=ws.col_values(8)[1:]
#         print(title)
#         for i , s in enumerate(status):
#             if s == "Pending":
#                 v=title[i]
#                 link = login.hw.getElement(f"//a[.='{v}']", "xpath")
#                 link.click()
#                 time.sleep(2)
#                 try:
#                     login.hw.getElement("//button[@name='OK']", "xpath").click()
#                     time.sleep(2)
#                 except:
#                     print("No Ok")
#                 time.sleep(4)
#                 score = login.hw.GetElementlistofattributeText(
#                         "//div[@class='gridCell']//span[@title='The numerical value used for rating calculations, for example 3.0.']//input[@type='text']",
#                         'xpath', 'value')
#                 print(score)
#                 label = login.hw.GetElementlistofattributeText(
#                         "//div[@class='gridCell']//span[@title='The short title or abbreviation of the rating increment. For example, Meets Expectations.']//input[@type='text']",
#                         'xpath', 'value')
#                 desc = login.hw.GetElementlistofText(
#                         "//div[@class='gridCell']//span[@title='The description of the rating increment. This is helpful to explain to your users how to use the rating.']/textarea",
#                         'xpath')
#                 sd = login.hw.GetElementText("//span[@class='ratingScaleTextArea']//textarea", "xpath")
#                 for j in values:
#                     if j['Scale Name'] == v:
#                         for ind, s in enumerate(score):
#                             ind+=2
#                             if str(j['Score'])==s:
#                                 format_cell_range(ws,f'D{j["ID"]+1}',green)
#                                 time.sleep(1)
#                             else:
#                                 format_cell_range(ws, f'D{j["ID"]+1}',red)
#                                 time.sleep(1)
#
#
#                         #
#                         #     else:
#                         #         su=login.hw.getElement(f"//span[@title='The numerical value used for rating calculations, for example 3.0.']//input[@value='{s}']",'xpath')
#                         #         su.send_keys(j['Score'])
#                         #         time.sleep(1)
#                         # login.hw.getElement('//span[@class=" icon icon_save"]','xpath').click()
#                         # time.sleep(1)
#
#                 time.sleep(1)
#                 login.hw.getElement("//span[@class=' icon icon_cancel']", "xpath").click()
#                 time.sleep(2)
#
#
#
#
#
#
#
#
#
#
#
#
# ob=AutomatedSap()
# ob.sheet_automat()
#
# import time
# import  gspread
# from gspread_formatting import *
# from task2 import SafScrape
# class AutomatedSap():
#     def sheet_automat(self):
#         login = SafScrape()
#         login.LoginSap()
#         red = CellFormat(
#             backgroundColor=Color(1, 0, 0), )
#         green = CellFormat(
#             backgroundColor=Color(0, 1, 0))
#         sa = gspread.service_account()
#         sh = sa.open('Net2apps')
#         ws = sh.get_worksheet(6)
#         values = ws.get_all_records()
#         status=ws.col_values(9)[1:]
#         title=ws.col_values(8)[1:]
#         for i , s in enumerate(status):
#             if s == "Pending":
#                 v=title[i]
#                 link = login.hw.getElement(f"//a[.='{v}']", "xpath")
#                 link.click()
#                 time.sleep(2)
#                 try:
#                     login.hw.getElement("//button[@name='OK']", "xpath").click()
#                     time.sleep(2)
#                 except:
#                     print("No Ok")
#                 time.sleep(4)
#
#                 score = login.hw.GetElementlistofattributeText(
#                     "//div[@class='gridCell']//span[@title='The numerical value used for rating calculations, for example 3.0.']//input[@type='text']",
#                     'xpath', 'value')
#                 label = login.hw.GetElementlistofattributeText(
#                         "//div[@class='gridCell']//span[@title='The short title or abbreviation of the rating increment. For example, Meets Expectations.']//input[@type='text']",
#                         'xpath', 'value')
#                 desc = login.hw.GetElementlistofText(
#                         "//div[@class='gridCell']//span[@title='The description of the rating increment. This is helpful to explain to your users how to use the rating.']/textarea",
#                         'xpath')
#                 sd = login.hw.GetElementText("//span[@class='ratingScaleTextArea']//textarea", "xpath")
#                 for j in values:
#                     if j['Scale Name'] == v:
#                         d = ws.acell(f'D{j["ID"]+1}').value
#                         s = login.hw.getElement(
#                             f"//span[@title='The numerical value used for rating calculations, for example 3.0.']//input[@value='{d}']",
#                             'xpath')
#                         if s==d:
#                             pass
#                         else:
#
#                             s.clear()
#                             s.send_keys(d)
#                             time.sleep(1)
#                             login.hw.getElement('//span[@class=" icon icon_save"]','xpath').click()
#                             time.sleep(1)
#
#
#                 time.sleep(1)
#                 login.hw.getElement("//span[@class=' icon icon_cancel']", "xpath").click()
#                 time.sleep(2)
#
#
# ob=AutomatedSap()
# ob.sheet_automat()
# import time
# import  gspread
# from gspread_formatting import *
# from task2 import SafScrape
# class AutomatedSap():
#     def sheet_automat(self):
#         login = SafScrape()
#         login.LoginSap()
#         red = CellFormat(
#             backgroundColor=Color(1, 0, 0), )
#         green = CellFormat(
#             backgroundColor=Color(0, 1, 0))
#         sa = gspread.service_account()
#         sh = sa.open('Net2apps')
#         ws = sh.get_worksheet(6)
#         values = ws.get_all_records()
#         status=ws.col_values(9)[1:]
#         title=ws.col_values(8)[1:]
#         for i , s in enumerate(status):
#             if s == "Pending":
#                 v=title[i]
#                 link = login.hw.getElement(f"//a[.='{v}']", "xpath")
#                 link.click()
#                 time.sleep(2)
#                 try:
#                     login.hw.getElement("//button[@name='OK']", "xpath").click()
#                     time.sleep(2)
#                 except:
#                     print("No Ok")
#                 time.sleep(4)
#
#                 score = login.hw.GetElementlistofattributeText(
#                     "//div[@class='gridCell']//span[@title='The numerical value used for rating calculations, for example 3.0.']//input[@type='text']",
#                     'xpath', 'value')
#                 label = login.hw.GetElementlistofattributeText(
#                         "//div[@class='gridCell']//span[@title='The short title or abbreviation of the rating increment. For example, Meets Expectations.']//input[@type='text']",
#                         'xpath', 'value')
#                 desc = login.hw.GetElementlistofText(
#                         "//div[@class='gridCell']//span[@title='The description of the rating increment. This is helpful to explain to your users how to use the rating.']/textarea",
#                         'xpath')
#                 sd = login.hw.GetElementText("//span[@class='ratingScaleTextArea']//textarea", "xpath")
#                 for j in values:
#                     if j['Scale Name'] == v:
#                         d = ws.acell(f'D{j["ID"]+1}').value
#                         s = login.hw.getElement(
#                             f"//span[@title='The numerical value used for rating calculations, for example 3.0.']//input[@value='{d}']",
#                             'xpath')
#                         if s==d:
#                             pass
#                         else:
#
#                             s.clear()
#                             s.send_keys(d)
#                             time.sleep(1)
#                             login.hw.getElement('//span[@class=" icon icon_save"]','xpath').click()
#                             time.sleep(1)
#
#
#                 time.sleep(1)
#                 login.hw.getElement("//span[@class=' icon icon_cancel']", "xpath").click()
#                 time.sleep(2)
#
#
# ob=AutomatedSap()
# ob.sheet_automat()
# #
# # if d != score_path:
# #     try:
# #         for b in dBtn:
# #             b.click()
# #             login.hw.getElement(
# #                 f'//a[@class="fd-link fd-link--compact ratingScaleSmallIconLinkPadding addRSValuesIcon"]',
# #                 'xpath').click()
# #             time.sleep(1)
# #             for a in score:
# #                 if score_path == None:
# #                     score_path.send_keys(d)
# #                     time.sleep(1)
# #                     login.hw.getElement('//span[@class=" icon icon_save"]', 'xpath').click()
# #                     time.sleep(1)
# #     except:
# #         print("no changes")
#
#         # if d != score_path:
#         #     try:
#         #         login.hw.getElement(
#         #             f'//a[@class="fd-link fd-link--compact ratingScaleSmallIconLinkPadding addRSValuesIcon"]',
#         #             'xpath').click().click()
#         #         for a in score:
#         #             size = len(score)
#         #             s = login.hw.GetElementByAttribute(
#         #                 f'(//table[@id = "66:m-m-tbl"]//tr//span[contains(@title, "numerical value")]//input)[{size - 1}]',
#         #                 'xpath', 'value')
#         #             print('Size',size-1)
#         #             s.send_keys(d)
#         #             time.sleep(1)
#         #             login.hw.getElement('//span[@class=" icon icon_save"]', 'xpath').click()
#         #             time.sleep(1)
#         #
#         #     except:
#         #         print('no Trash')
#
# _obj_Srch_Field = "//table[@class='MDFSearchBar']//tr//td[contains(text(),'Search')]/following-sibling::td[1]/span[3]//input"
#         object_id_list = []
#
#         searchBox_id = str(self._selenium.getElementAttributeText(_obj_Srch_Field, "id", By.XPATH, True)).split("__")[0] + "_"
#
#         Browser.DRIVER.execute_script("ECTUtil.getComponentById('" + searchBox_id + "')._model._searchFields.pageSize = 2000")
#
#
#         objects_list_dict =  Browser.DRIVER.execute_script("return ECTUtil.getComponentById('" + searchBox_id + "')._model._searchDAO._staticData.results;")
#
#
# time.sleep(2)
# element = call_login.hw.getElement('(//input[@aria-autocomplete="list"])[2]', 'xpath')
# element.send_keys(f'{key}')
# time.sleep(3)
# call_login.hw.getElement('//a[@role="menuitem"]', 'xpath').click()
# time.sleep(3)
# element.clear()


link = login.hw.getElement(f"//a[.='{i}']", "xpath")
link.click()
time.sleep(1)
try:
    login.hw.getElement("//button[@name='OK']", "xpath").click()
    time.sleep(1)
except:
    print("no Ok")

score = login.hw.GetElementlistofattributeText(
    "//div[@class='gridCell']//span[@title='The numerical value used for rating calculations, for example 3.0.']//input[@type='text']",
    'xpath', 'value')
label = login.hw.GetElementlistofattributeText(
    "//div[@class='gridCell']//span[@title='The short title or abbreviation of the rating increment. For example, Meets Expectations.']//input[@type='text']",
    'xpath', 'value')
desc = login.hw.GetElementlistofText(
    "//div[@class='gridCell']//span[@title='The description of the rating increment. This is helpful to explain to your users how to use the rating.']/textarea",
    'xpath')
sd = login.hw.GetElementText("//span[@class='ratingScaleTextArea']//textarea", "xpath")
for r, s in enumerate(score):

    if s == v['Score']:
        format_cell_range(ws, f'D{v["ID"] + 1}', green)
        time.sleep(1)
    else:
        format_cell_range(ws, f'D{v["ID"] + 1}', red)

    # if label[r] == v['Score Label']:
    #     format_cell_range(ws, f'E{id}', green)
    #     time.sleep(1)
    # else:
    #     format_cell_range(ws, f'E{id}', red)

time.sleep(1)
login.hw.getElement("//span[@class=' icon icon_cancel']", "xpath").click()
time.sleep(1)
v["Status"] = 'Processed'
ws.update_acell(f'I{v["ID"] + 1}', 'Processed')

import time
import  gspread
from  Login import  *
class AutomatedSap():
    Login()
    def sheet_automat(self):

        curl = driver.current_url
        d = curl.split("=")[-1]
        rurl = "https://pmsalesdemo8.successfactors.com/acme?fbacme_o=admin&pess_old_admin=true&ap_param_action=form_rating_scale&itrModule=talent&_s.crb=%s"
        rate_url = rurl % d
        driver.get(rate_url)
        time.sleep(2)
        sa = gspread.service_account()
        sh = sa.open('Net2apps')
        ws = sh.get_worksheet(6)
        values = ws.get_all_records()
        status=ws.col_values(9)[1:]
        title=ws.col_values(8)[1:]
        for i , s in enumerate(status):
            if s == "Pending":
                v=title[i]
                link = hw.getElement(f"//a[.='{v}']", "xpath")
                link.click()
                time.sleep(1)
                try:
                    hw.getElement("//button[@name='OK']", "xpath").click()
                    time.sleep(1)
                except:
                    print("No Ok")
                time.sleep(2)
                score = hw.GetElementlistofattributeText('//table[@id = "66:m-m-tbl"]//tr//span[contains(@title, "numerical value")]//input','xpath', 'value')
                label = hw.GetElementlistofattributeText('//table[@id = "66:m-m-tbl"]//tr//span[contains(@title, "title or abbreviation")]//input','xpath', 'value')
                desc =  hw.GetElementlistofText('//table[@id = "66:m-m-tbl"]//tr//span[contains(@title, "The description")]//textarea','xpath')

                sd = hw.GetElementText("//span[@class='ratingScaleTextArea']//textarea", "xpath")
                dBtn=hw.getElements('//a[@class="fd-link fd-link--compact ratingScaleSmallIconPadding deleteIcon"]','xpath')
                ind=0
                size = len(score)
                for j in values:
                    if j['Scale Name'] == v:
                        ind+=1
                        d = ws.acell(f'D{j["ID"] + 1}').value
                        l = ws.acell(f'E{j["ID"] + 1}').value
                        ds = ws.acell(f'F{j["ID"] + 1}').value
                        score_path = hw.GetElementByAttribute(
                            f'(//table[@id = "66:m-m-tbl"]//tr//span[contains(@title, "numerical value")]//input)[{ind}]',
                            'xpath','value')

                        if d != score_path:
                            hw.getElement('//a[@class="fd-link fd-link--compact ratingScaleSmallIconLinkPadding addRSValuesIcon"]','xpath').click()
                            time.sleep(1)
                            size+=1
                            s = hw.getElement(
                                    f'(//table[@id = "66:m-m-tbl"]//tr//span[contains(@title, "numerical value")]//input)[{size}]',
                                    'xpath')
                            ls=hw.getElement(f'(//table[@id = "66:m-m-tbl"]//tr//span[contains(@title, "title or abbreviation")]//input)[{size}]','xpath')
                            sd=hw.getElement(f'(//table[@id = "66:m-m-tbl"]//tr//span[contains(@title, "The description")]//textarea)[{size}]','xpath')
                            s.send_keys(d)
                            time.sleep(1)
                            ls.send_keys(l)
                            time.sleep(1)
                            sd.send_keys(ds)
                            time.sleep(1)
                            try:
                                hw.getElement("//button[.='OK']",'xpath').click()
                                time.sleep(1)
                            except:
                                print("no Ok")
                            hw.getElement('//span[@class=" icon icon_save"]', 'xpath').click()
                            time.sleep(1)

                time.sleep(1)
                hw.getElement("//span[@class=' icon icon_cancel']", "xpath").click()
                time.sleep(1)


ob=AutomatedSap()
ob.sheet_automat()