#!/usr/bin/env bash

sqlite3 test.db "DELETE FROM Convert;"
python Zeugnisliste/addToConvertTable.py
python main.py
flatpak run org.libreoffice.LibreOffice Zegnislisteneu.docx
