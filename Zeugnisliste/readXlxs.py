
def readXlxs():
    """get data from .xlxs file"""
    wb = Workbook('test.xlxs')
    wb = openpyxl.load_workbook('test.xlsx')
    ws = wb.active
    #print(wb.sheetnames)
    sheet = wb['Zeugnisnoten_Abschluss']
    for i in range(1,36):
        print(sheet.cell(row=1, column=i).value, "  Spalte", i)

if __name__ == "__main__":
    readXlxs()
