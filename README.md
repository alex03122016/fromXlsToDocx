
Aim
-------------------------------------------------------------------------------
Copy Data from .xlxs file to docx file.

install
-------------------------------------------------------------------------------
venv
#sqlite3 for ubuntu
sudo apt-get install sqlite3
pip install SQLAlchemy

pip install python-docx
pip install openpyxl

setup
-------------------------------------------------------------------------------
* run, adds Convert Data to Database test.db
'code python Zeugnisliste/addToConvertTable.py'
+ run to copy the data from test.xls to Zeugnisliste.docx
'python main.py'
