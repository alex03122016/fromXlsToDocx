

def addToConvertTable():
    """add convert data to database"""
        #prepare convert data
        fieldsNoten =["Deu_ins", "Deu_m", "Deu_s", "Englisch", "GeWi_ins", "Geo",
                "Geschichte", "politischeBildung", "Ethik", "WAT", "Ma",
                "NaWi_ins", "Bio", "Che", "Phy", "Ku", "Mu", "Sp"]

        #[fieldName][Column Integer or None]
        fieldsNotenSeite1 =[  ["Deu_ins",4],
                        ["Deu_m",None],
                        ["Deu_s",None],
                        ["Englisch", 10],
                        ["GeWi_ins",None],
                        ["Geo",None],
                        ["Geschichte",None],
                        ["politischeBildung",None],
                        ["Ethik", 12],
                        ["WAT",None],
                        ["Ma",11],
                        ["NaWi_ins", 13],
                        ["Bio",None],
                        ["Che",None],
                        ["Phy",None],
                        ["Ku",None],
                        ["Mu",None],
                        ["Sp", None],
                        ]

        #fieldsSchuelerSeite1
        #fieldsSchuelerSeite3
        #fieldsNotenSeite2
        #fieldsNotenSeite3
        #fieldsNotenSeite4
        #fieldsFehlzeitenSeite4

        fieldsNotenQuelle =[  ["Deu_ins",8],
                        ["Deu_m",9],
                        ["Deu_s",10],
                        ["Englisch", 11],
                        ["GeWi_ins",12],
                        ["Geo",13],
                        ["Geschichte",14],
                        ["politischeBildung",None],
                        ["Ethik", 12],
                        ["WAT",None],
                        ["Ma",19],
                        ["NaWi_ins", 20],
                        ["Bio",21],
                        ["Che",22],
                        ["Phy",23],
                        ["Ku",24],
                        ["Mu",25],
                        ["Sp", 26],
                        ]

    SchuelerId = 0
    SchuelerRow = 3
    fach = 0
    for SchuelerId in range(0, 9):
        fach = 0

        for element in fieldsNotenSeite1:
            if element[1] is not None:


                print("Schueler" + str(SchuelerId)+ element[0],
                                "Column", element[1],
                                "Row", SchuelerRow)


                data = Convert(field="Schueler" + str(SchuelerId)+ element[0],
                                column_Zeugnisliste=element[1],
                                row_Zeugnisliste = SchuelerRow,
                                column_calctable= fieldsNotenQuelle[fach][1],
                                row_calctable= SchuelerId +1
                                )
                session.add(data)
                session.commit()
            if fach + 1 < len(fieldsNotenQuelle):
                fach = fach + 1
                print("fach:    ", fach,
                        "SchuelerId", SchuelerId)
        SchuelerId = SchuelerId + 1
        SchuelerRow = SchuelerRow + 3

if __name__ == "__main__":
    addToConvertTable()
