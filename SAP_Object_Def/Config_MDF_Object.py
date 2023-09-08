import time
from gspread_formatting import *


class Config():
    cell_red = CellFormat(
    backgroundColor=Color(1, 0, 0), )
    cell_green = CellFormat(
    backgroundColor=Color(0, 1, 0))
    def red_url(self,driver,hw):
        curl = driver.current_url
        d = curl.split("=")[-1]
        rurl = "https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=%s"
        rate_url = rurl % d
        driver.get(rate_url)
        # Home url End
        time.sleep(0.5)
        hw.ClickElement("19__write_toggle", "id")
        time.sleep(0.5)
        hw.ClickElement('//a[@title="Object Definition"]', 'xpath')
        time.sleep(0.5)
        hw.ClickElement("9__write_toggle", "id")
        # object Click dropdown



