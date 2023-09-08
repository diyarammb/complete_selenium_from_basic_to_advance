import gspread
def ws_con(n):
    sa = gspread.service_account()
    sh = sa.open('Net2apps')
    ws=sh.get_worksheet(n)
    return ws
