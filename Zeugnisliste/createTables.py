
def createTables():
    #create tables
    alltables = [Schuljahr, Fehlzeiten, Noten, ZeugnislisteDokument, Convert]
    for table in alltables:
        table.__table__.create(engine)"""
    #Convert.__table__.create(engine)
