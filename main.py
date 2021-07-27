
from Zeugnisliste.configuration import *
def fromXlxsToDocx():

    #transfer of data
    for i in range(1,221):
        #get coordinates data from Convert sqlite3
        data = session.query(Convert).filter_by(id=i).all()
        data = data[0]
        #get values  of fields in .xlxs file
        sourceValue = sheet.cell(row=data.row_calctable+1, column=data.column_calctable).value
        #get coordinates of field in .docx file
        r = data.row_Zeugnisliste
        c = data.column_Zeugnisliste
        tableDocx = doc.tables[data.table_zeugnisliste]
        targetCell = tableDocx.cell(r, c)
        targetCellValue = targetCell.text
        #write data  to .docxf file
        targetCell.text = str(sourceValue)

    doc.save(savepath)

if __name__ == "__main__":
    fromXlxsToDocx()
