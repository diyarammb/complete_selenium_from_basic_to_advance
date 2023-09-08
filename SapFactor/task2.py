import time
from gspread import Cell
from gspread_formatting import DataValidationRule, BooleanCondition, set_data_validation_for_cell_range
import  gspread
from Login import *
def ScrapeData(hw):
        Login()
        sa = gspread.service_account()
        sh = sa.open('Net2apps')
        ws = sh.get_worksheet(4)
        curl = driver.current_url
        d = curl.split("=")[-1]
        rurl = "https://pmsalesdemo8.successfactors.com/acme?fbacme_o=admin&pess_old_admin=true&ap_param_action=form_rating_scale&itrModule=talent&_s.crb=%s"
        rate_url = rurl % d
        driver.get(rate_url)
        time.sleep(2)
        aElement=hw.GetElementlistofText("//a[@class='fd-link fd-link--compact']","xpath")
        ValidationRule = DataValidationRule(
            BooleanCondition('ONE_OF_LIST', ['Pending', 'Processed']),
            showCustomUi=True)
        id=1
        h=1
        cell_list=[]
        for e, i in enumerate(aElement):
            h+=1
            cell_list.append(Cell(row=h, col=8, value=i))
            ws.update_cells(cell_list)
            time.sleep(1)
            set_data_validation_for_cell_range(ws, 'I2:I16', ValidationRule)
            link=hw.getElement(f"//a[.='{i}']","xpath")
            link.click()
            time.sleep(2)
            try:
                hw.getElement("//button[@name='OK']", "xpath").click()
                time.sleep(1)

            except:
                print("Ok Not Click")
            score = hw.GetElementlistofattributeText(
                            "//div[@class='gridCell']//span[@title='The numerical value used for rating calculations, for example 3.0.']//input[@type='text']",
                            'xpath', 'value')
            label = hw.GetElementlistofattributeText(
                            "//div[@class='gridCell']//span[@title='The short title or abbreviation of the rating increment. For example, Meets Expectations.']//input[@type='text']",
                            'xpath', 'value')
            desc = hw.GetElementlistofText(
                            "//div[@class='gridCell']//span[@title='The description of the rating increment. This is helpful to explain to your users how to use the rating.']/textarea",
                            'xpath')
            sd = hw.GetElementByAttribute("//span[@class='ratingScaleTextArea']//textarea", "xpath",'value')

            for r ,s in enumerate(score):
                id+=1
                cell_list.append(Cell(row=id, col=2, value=i))
                cell_list.append(Cell(row=id, col=4, value=s))
                cell_list.append(Cell(row=id, col=5, value=label[r]))
                cell_list.append(Cell(row=id, col=6, value=desc[r]))
                cell_list.append(Cell(row=id, col=3, value=sd))
            hw.getElement("//span[@class=' icon icon_cancel']","xpath").click()
            time.sleep(1)
        ws.update_cells(cell_list)

ScrapeData(hw)