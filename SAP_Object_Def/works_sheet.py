import gspread
def works_sheet(name):
    sa = gspread.service_account()
    sh = sa.open('Net2apps')
    ws=sh.worksheet(name)
    return ws
