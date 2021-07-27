
from Zeugnisliste.configuration import *


def readDatabase():

    for i in range(1,82):
        #get coordinates data from Convert sqlite3
        data = session.query(Convert).filter_by(id=i).all()
        data = data[0]
        print(  data.id,
                data.field,
                data.row_Zeugnisliste,
                data.column_Zeugnisliste,
                "table", data.table_zeugnisliste,
                data.row_calctable,
                data.column_calctable
                )
if __name__ == "__main__":
    readDatabase()
