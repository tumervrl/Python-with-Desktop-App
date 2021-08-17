#-----------------------------Library-------------------------#

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from HomePageUI import *


Uygulama=QApplication(sys.argv)
AnaPen=QMainWindow()
ui=Ui_MainWindow()

ui.setupUi(AnaPen)
AnaPen.show()

# ---------------------------DataBase--------------------------#

import sqlite3


global curs
global conn

conn = sqlite3.connect('veritabani.db')
curs = conn.cursor()

sorguCreTbl = (" CREATE TABLE IF NOT EXISTS urun(          \
              Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,  \
              UrunAdi TEXT NOT NULL UNIQUE ,               \
              SatisFiyati TEXT NOT NULL,             \
              AlisFiyati TEXT NOT NULL,            \
              StokAdedi TEXT NOT NULL,         \
              Kategori TEXT NOT NULL,           \
              Dtarihi TEXT NOT NULL )")
curs.execute(sorguCreTbl)
conn.commit()
#---------------------------Application-----------------------#

def ekle():
    _urunadi = ui.urunadi.text()
    _satisfiyati = ui.satisfiyati.text()
    _alisfiyati = ui.alisfiyati.text()
    _stokadedi = ui.stokadedi.text()
    _kategori = ui.kategori.text()
    _calwdt = ui.calwdt.selectedDate().toString(QtCore.Qt)


    curs.execute("INSERT INTO urun  \
                   (UrunAdi,SatisFiyati,AlisFiyati,StokAdedi,Kategori,Dtarihi)  \
                   VALUES (?,?,?,?,?,?)",  \
                   (_urunadi,_satisfiyati_alisfiyati,_stokadedi,_kategori,_calwdt))
    conn.commit()




#---------------------------Signal--------------------------#

ui.btnekle.clicked.connect(ekle)



sys.exit(Uygulama.exec_())









