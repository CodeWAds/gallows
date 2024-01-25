from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QStackedLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtCore import QUrl
from translator import translate_start

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.create_window()

    def create_window(self):
        self.setObjectName("MainWindow")
        self.setFixedSize(720, 480)
        self.setStyleSheet("background-color: rgb(140, 83, 255);\n"
                           "font: 16pt \"Fixedsys\"")
        self.StartMenu()

    def StartMenu(self):

        # Название игры в окне
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # установка изображения языка
        self.label_flag = QLabel(self)
        self.label_flag.setGeometry(QtCore.QRect(26, 10, 31, 31))
        self.image_paths = ['src/language/RF.png', 'src/language/UK.png']
        self.current_image_index = 0
        self.loadImage()
        self.label_flag.setObjectName("label_flag")

        # иконка
        icon = QIcon("src/stages_with_bg/stage_6.png")
        self.setWindowIcon(icon)

        self.name_game = QLabel(self)
        self.name_game.setGeometry(QtCore.QRect(310, 100, 100, 20))
        self.name_game.setStyleSheet("font-size: 20pt;")
        self.name_game.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_game.setObjectName("name_game")
        self.name_game.setText("Виселица")

        self.lang_button = QPushButton(self)

        self.lang_button.setGeometry(QtCore.QRect(10, 40, 70, 30))
        self.lang_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.lang_button.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        self.lang_button.setAutoFillBackground(False)
        self.lang_button.setStyleSheet("QPushButton{border: 1px solid #dfe6e9;\n"
                                       "background-color: #a29bfe;\n"
                                       "border-radius: 5px;\n"
                                       "font: 12pt \"Fixedsys\";}\n"
                                       "QPushButton:hover { background-color: #8c7ae6; }"
                                       "")
        self.lang_button.setObjectName("lang_button")
        self.lang_button.setText("Сменить\n"
                                 "язык")
        self.lang_button.clicked.connect(self.change_lang)

        self.start_button = QPushButton(self)

        self.start_button.setGeometry(QtCore.QRect(280, 260, 160, 40))
        self.start_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.start_button.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        self.start_button.setAutoFillBackground(False)
        self.start_button.setStyleSheet("QPushButton{border: 1px solid #dfe6e9;\n"
                                        "background-color: #a29bfe;\n"
                                        "border-radius: 5px;\n"
                                        "padding: 50px;}\n"
                                        "QPushButton:hover { background-color: #8c7ae6; }"
                                        "")
        self.start_button.setObjectName("start_button")
        self.start_button.setText("СТАРТ")
        self.start_button.clicked.connect(self.category_game)

        self.setCentralWidget(self.centralwidget)

        self.setWindowTitle("Виселица")

    def category_game(self):
        self.category_widget = QWidget(self)
        self.category_widget.setObjectName("category_widget")

        name_cat = QLabel(self.category_widget)
        name_cat.setGeometry(QtCore.QRect(310, 100, 100, 20))
        name_cat.setStyleSheet("font-size: 20pt;")
        name_cat.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        name_cat.setObjectName("name_game")
        name_cat.setText("Категория")

        hardware_button = QPushButton(self.category_widget)
        hardware_button.setGeometry(QtCore.QRect(140, 260, 147, 39))
        hardware_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        hardware_button.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        hardware_button.setAutoFillBackground(False)
        hardware_button.setStyleSheet("QPushButton{border: 1px solid #dfe6e9;\n"
                                      "background-color: #a29bfe;\n"
                                      "border-radius: 5px;\n"
                                      "font: 12pt \"Fixedsys\";}\n"
                                      "QPushButton:hover { background-color:#8c7ae6; }"
                                      "")
        hardware_button.setObjectName("hardware_button")
        hardware_button.setText("Аппаратное\n"
                                "обеспечение")
        hardware_button.clicked.connect(self.hardware)

        software_button = QPushButton(self.category_widget)

        software_button.setGeometry(QtCore.QRect(292, 260, 147, 39))
        software_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        software_button.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        software_button.setAutoFillBackground(False)
        software_button.setStyleSheet("QPushButton{border: 1px solid #dfe6e9;\n"
                                      "background-color: #a29bfe;\n"
                                      "border-radius: 5px;\n"
                                      "font: 12pt \"Fixedsys\";}\n"
                                      "QPushButton:hover { background-color: #8c7ae6; }"
                                      "")
        software_button.setObjectName("soft_button")
        software_button.setText("Программное\n"
                                "обеспечение")
        software_button.clicked.connect(self.software)

        internet_button = QPushButton(self.category_widget)

        internet_button.setGeometry(QtCore.QRect(444, 260, 147, 39))
        internet_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        internet_button.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        internet_button.setAutoFillBackground(False)
        internet_button.setStyleSheet("QPushButton{border: 1px solid #dfe6e9;\n"
                                      "background-color: #a29bfe;\n"
                                      "border-radius: 5px;\n"
                                      "font: 12pt \"Fixedsys\";}\n"
                                      "QPushButton:hover { background-color: #8c7ae6; }"
                                      "")
        internet_button.setObjectName("internet_button")
        internet_button.setText("Интернет")
        internet_button.clicked.connect(self.internet)

        self.setCentralWidget(self.category_widget)

        if self.current_image_index != 0:
            name_cat.setText("Category")
            hardware_button.setText("Hardware")
            software_button.setText("Software")
            internet_button.setText("Internet")


    def hardware(self):
        self.hardware_widget = QWidget(self)
        self.hardware_widget.setObjectName("hardware_widget")
        self.game(self.hardware_widget)

        self.setCentralWidget(self.hardware_widget)
    
    def software(self):
        self.software_widget = QWidget(self)
        self.software_widget.setObjectName("software_widget")
        self.game(self.software_widget)

        self.setCentralWidget(self.software_widget)

    def internet(self):
        self.internet_widget = QWidget(self)
        self.internet_widget.setObjectName("internet_widget")
        self.game(self.internet_widget)

        self.setCentralWidget(self.internet_widget)


    def game(self,widget):
        
        gallows_picture = QLabel(widget)
        gallows_picture.setGeometry(QtCore.QRect(10, 10, 301, 281))
        pixmap_gallow = QPixmap("src/stages_with_bg/stage_0.png")
        gallows_picture.setPixmap(pixmap_gallow)
        self.resize(pixmap_gallow.width(), pixmap_gallow.height())
        gallows_picture.setObjectName("gallow_picture")

        english_keys = [
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
        ]

        russian_keys = [
            ['Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ'],
            ['Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж', 'Э'],
            ['Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю']
        ]

        if self.current_image_index == 0:
            keyboard = russian_keys
        else:
            keyboard = english_keys
        label_keyboard = QLabel(widget)
        label_keyboard.setGeometry(QtCore.QRect(10, 316, 701, 151))
        keyboard_layout = QVBoxLayout(label_keyboard)

        for row in keyboard:
            key_row = QHBoxLayout()
            for key in row:
                button_keyboard = QPushButton(key)
                key_row.addWidget(button_keyboard)
                button_keyboard.setStyleSheet("QPushButton{border: 1px solid #dfe6e9;\n"
                                              "background-color: #a29bfe;\n"
                                              "border-radius: 5px;\n"
                                              "font: 20pt \"Fixedsys\";}\n"
                                              "QPushButton:hover { background-color: #8c7ae6; }"
                                              "")
                button_keyboard.setCursor(QtGui.QCursor(
                    QtCore.Qt.CursorShape.PointingHandCursor))

            keyboard_layout.addLayout(key_row)

       

    # def start_again(self):
    #     self.category_widget.hide()

    def loadImage(self):
        pixmap = QPixmap(self.image_paths[self.current_image_index])
        self.label_flag.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

    def change_lang(self):
        self.current_image_index = (
            self.current_image_index + 1) % len(self.image_paths)
        self.loadImage()
        if self.current_image_index == 0:
            self.start_button.setText("СТАРТ")
            self.name_game.setText("Виселица")
            self.lang_button.setText("Сменить\n"
                                     "язык")
            self.setWindowTitle("Виселица")

        else:
            self.start_button.setText(translate_start["СТАРТ"])
            self.name_game.setText(translate_start["Виселица"])
            self.lang_button.setText(translate_start["Сменить\n"
                                                     "язык"])
            self.setWindowTitle(translate_start["Виселица"])


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
