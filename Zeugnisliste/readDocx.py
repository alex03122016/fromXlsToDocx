def readDocx():
    """ analyze target docx file """
    savepath= "Zegnislisteneu.docx"
    doc = docx.Document('Zeugnisliste.docx')
    for i in range(len(doc.paragraphs)):
        print("Paragraph",i, doc.paragraphs[i].text)
    table1 = doc.tables[0]
    cell = table1.cell(2,1)
    print("cell", cell.text)

    reihe = 0
    spalte = 0

    for row in table1.rows:

        for cell in row.cells:
            print("Reihe",reihe, "Spalte", spalte, cell.text)
            spalte = spalte + 1
        reihe = reihe + 1
        spalte = 0

    doc.save(savepath)

if __name__ == "__main__":
    readDocx()
