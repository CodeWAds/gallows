from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore, QtGui, QtWidgets
from translator import translate_start
import sys


class CategoryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ChoiceCategory()

    def ChoiceCategory(self):
        self.setObjectName("CategoryWindow")
        self.setFixedSize(720, 480)
        self.setStyleSheet("background-color: rgb(140, 83, 255);\n"
                           "font: 16pt \"Fixedsys\"")
        self.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget1")
        
        
        
# app = QApplication(sys.argv)
# window = CategoryWindow()
# window.show()
# app.exec()