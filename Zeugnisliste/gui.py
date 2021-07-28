
import tkinter as tk
#from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.filedialog import asksaveasfile

from tkinter import *
from tkinter.ttk import *
#from Zeugnisliste import *
from fromXlxsToDocx import *
#from configuration import *


def gui():
    #colorsyllables
    def copyToDocx ():
        print("staring ...")
        print(selectXlsxFile.filename)
        fromXlxsToDocx( xlsxFile=selectXlsxFile.filename,
                        outputDocx= saveDocx.docxFile)

    def selectXlsxFile():
        filetypes = (
            ('.xlsx', '*.xlsx'),
            ('All files', '*.*')
        )
        selectXlsxFile.filename = fd.askopenfilename(
        title='Öffne eine Datei',
        initialdir='~',
        filetypes=filetypes)

        showinfo(
            title='Ausgewewäte Datei',
            message=selectXlsxFile.filename
        )
        print(selectXlsxFile.filename)

    def saveDocx():
        files = [('All Files', '*.*'),
                 ('.docx', '*.docx')]
        saveDocx.docxFile = asksaveasfile(  filetypes = files,
                                            defaultextension = files)

    app = tk.Tk()
    #p1 = PhotoImage(file = 'learny.png')

    #app.iconphoto(False, p1)
    app.title("Zeugnisliste")
    canvas1 = tk.Canvas(app, width = 400, height = 300)
    canvas1.configure(background="lightgreen")




    #let user define name of input file xlxs
    openXlxsFile_Btn = tk.Button(   text='Öffnen der Quelle',
                                    command=selectXlsxFile)
    openXlxsFile_Btn.configure(   background="green",
                                    fg='#ffffff',
                                    borderwidth=0)
    canvas1.create_window(300, 220, window=openXlxsFile_Btn)

    #let user define target file Zeugnisliste
    saveDocx_Btn = tk.Button(   text='Speicherort',
                                    command=saveDocx)
    saveDocx_Btn.configure(   background="green",
                                    fg='#ffffff',
                                    borderwidth=0)
    canvas1.create_window(100, 270, window=saveDocx_Btn)



    #let user define location and name of database

    #button for create tables in Database
    copyToDocx_Btn = tk.Button( text='kopieren nach docx',
                                    command=copyToDocx)
    copyToDocx_Btn.configure(   background="green",
                                    fg='#ffffff',
                                    borderwidth=0)
    canvas1.create_window(100, 220, window=copyToDocx_Btn)
    canvas1.pack()
    #button for add data to convert table
    #button for read table
    #button for copying script: main

    app.mainloop()

if __name__ == "__main__":
    gui()
