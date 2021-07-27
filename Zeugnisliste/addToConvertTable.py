
from configuration import *


def addToConvertTable():

    """add convert data to database"""
    #[fieldName,        Column Integer or None,        table 0 or 1]
    fieldsNotenSeite1 =[
                    ["name",1,0],
                    ["vorname",2,0],
                    ["geburtsdatum",3,0],
                    ["Deu_ins",4,0],
                    ["Deu_m",None,None],
                    ["Deu_s",None,None],
                    ["Englisch", 10,0],
                    ["GeWi_ins",1,1],
                    ["Geo",None,None],
                    ["Geschichte",None,None],
                    ["politischeBildung",None,None],
                    ["Ethik", 12,0],
                    ["WAT",None,None],
                    ["Ma",11,0],
                    ["NaWi_ins", 13,0],
                    ["Bio",None,None],
                    ["Che",None,None],
                    ["Phy",None,None],
                    ["Ku",2,1],
                    ["Mu",3,1],
                    ["Sp", 4,1],
                    ["T_ins", 6,1],
                    ["T_ue", 7,1],
                    ["Stu", 8,1],
                    ["Stu_ue", 9,1],
                    ["v", 10,1],
                    ]
    # coordinates from source .xlxs file
    fieldsNotenQuelle =[
                    ["name",1],
                    ["vorname",2],
                    ["geburtsdatum",4],
                    ["Deu_ins",8],
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
                    ["T_ins", 31],
                    ["T_ue", 32],
                    ["Stu", 33],
                    ["Stu_ue", 33],
                    ["v", 34],
                    ]

    SchuelerId = 0
    SchuelerRow = 3
    fach = 0
    hasReachedNine = False
    for i in range(0, 13):
        fach = 0
        hasReachedNineTable = False
        for element in fieldsNotenSeite1:
            if element[1] is not None:


                if i == 9 and hasReachedNine == False:
                    SchuelerRow = SchuelerRow - 27
                    hasReachedNine = True
                if i >= 9:
                    tableZeugnislisteConvert = element[2] + 2
                else:
                    tableZeugnislisteConvert = element[2]

                #if data is for table [1] lift it up by one row and one to the left
                if element[2] == 1:
                    SchuelerRowConvert = SchuelerRow - 1
                    columnZeugnislisteConvert = element[1] -1
                else:
                    SchuelerRowConvert = SchuelerRow
                    columnZeugnislisteConvert = element[1]
                print("Schueler" + str(SchuelerId)+ element[0],
                                "Column", element[1],
                                "Row", SchuelerRow,
                                "Table", tableZeugnislisteConvert)

                data = Convert(field="Schueler" + str(SchuelerId)+ element[0],
                                column_Zeugnisliste=columnZeugnislisteConvert,
                                row_Zeugnisliste = SchuelerRowConvert,
                                table_zeugnisliste = tableZeugnislisteConvert,
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
