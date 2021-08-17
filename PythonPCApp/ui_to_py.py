from PyQt5 import uic

with open('HomePageUI.py', 'w',encoding="utf-8") as fout:
    uic.compileUi('HomePage.ui',fout)