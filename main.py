from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QStackedLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtMultimedia import *
from PyQt6.QtCore import QUrl
import random
import translator

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.create_window()

    def create_window(self):
        self.setObjectName("MainWindow")
        self.setFixedSize(720, 480)
        self.setStyleSheet("background-color: rgb(140, 83, 255);\n"
                           "font: 14pt \"Comic Sans MS\"")
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
        self.load_image()
        self.label_flag.setObjectName("label_flag")

        # иконка
        icon = QIcon("src/stages_with_bg/stage_6.png")
        self.setWindowIcon(icon)

        self.name_game = QLabel(self)
        self.name_game.setGeometry(QtCore.QRect(280, 100, 160, 50))
        self.name_game.setStyleSheet("font-size: 25pt;")
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
                                       "font: 7pt \"Comic Sans MS\";}\n"
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
                                        "padding: 50px;\n"
                                        "font: 13pt Comic Sans MS}"
                                        "QPushButton:hover { background-color: #8c7ae6; }"
                                        "")
        self.start_button.setObjectName("start_button")
        self.start_button.setText("СТАРТ")
        self.start_button.clicked.connect(self.category_game)

        self.setCentralWidget(self.centralwidget)

        self.setWindowTitle("Виселица")

    def category_game(self):
        self.sound_button()
        self.category_widget = QWidget(self)
        self.category_widget.setObjectName("category_widget")

        name_category = QLabel(self.category_widget)
        name_category.setGeometry(QtCore.QRect(280, 100, 160, 50))
        name_category.setStyleSheet("font-size: 25pt;")
        name_category.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        name_category.setObjectName("name_game")
        name_category.setText("Категория")

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
                                      "font: 10pt \"Comic Sans MS\";}\n"
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
                                      "font: 10pt \"Comic Sans MS\";}\n"
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
                                      "font: 10pt \"Comic Sans MS\";}\n"
                                      "QPushButton:hover { background-color: #8c7ae6; }"
                                      "")
        internet_button.setObjectName("internet_button")
        internet_button.setText("Интернет")
        internet_button.clicked.connect(self.internet)

        self.setCentralWidget(self.category_widget)

        if self.current_image_index != 0:
            name_category.setText("Category")
            hardware_button.setText("Hardware")
            software_button.setText("Software")
            internet_button.setText("Internet")

    def hardware(self):
        self.sound_button()
        self.hardware_widget = QWidget(self)
        self.hardware_widget.setObjectName("hardware_widget")
        self.category_words = 1
        self.generate_word()
        self.game(self.hardware_widget)

        self.setCentralWidget(self.hardware_widget)

    def software(self):
        self.sound_button()
        self.software_widget = QWidget(self)
        self.software_widget.setObjectName("software_widget")
        self.category_words = 2
        self.generate_word()
        self.game(self.software_widget)

        self.setCentralWidget(self.software_widget)

    def internet(self):
        self.sound_button()
        self.internet_widget = QWidget(self)
        self.internet_widget.setObjectName("internet_widget")
        self.category_words = 3
        self.generate_word()
        self.game(self.internet_widget)

        self.setCentralWidget(self.internet_widget)

    def game(self, widget):

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
                                              "font: 10pt \"Comic Sans MS\";}\n"
                                              "QPushButton:hover { background-color: #8c7ae6; }"
                                              "")
                button_keyboard.setCursor(QtGui.QCursor(
                    QtCore.Qt.CursorShape.PointingHandCursor))

            keyboard_layout.addLayout(key_row)
        label_keyboard.setObjectName("label_keyboard")
        open_word = QLabel(widget)
        open_word.setGeometry(QtCore.QRect(320, 90, 391, 41))
        open_word.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        open_word.setStyleSheet("font-size: 20pt;")
        open_word.setText(self.word_shown)
        open_word.setObjectName("open_word")

        hidden_word = QLabel(widget)
        hidden_word.setGeometry(QtCore.QRect(320, 200, 391, 41))
        hidden_word.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        hidden_word.setStyleSheet("font-size: 20pt;")
        hidden_word.setText("_ _ _ _ _ _ _ _")
        hidden_word.setObjectName("hidden_word")

    def sound_button(self):
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        self.player.setSource(QUrl.fromLocalFile("src/sounds/buttons.wav"))
        self.audioOutput.setVolume(50)
        self.player.play()

    def generate_word(self):
        if self.category_words == 1:
            _words = translator.words_hardware_ru
        elif self.category_words == 2:
            _words = translator.words_software_ru
        else:
            _words = translator.words_internet_ru
        word_of_items = list(_words.items())
        s = random.randint(0,len(_words)-1)
        self.word_shown = word_of_items[s][0]
       



    # def start_again(self):
    #     self.category_widget.hide()

    def load_image(self):
        pixmap = QPixmap(self.image_paths[self.current_image_index])
        self.label_flag.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

    def change_lang(self):
        self.sound_button()
        self.current_image_index = (
            self.current_image_index + 1) % len(self.image_paths)
        self.load_image()
        if self.current_image_index == 0:
            self.start_button.setText("СТАРТ")
            self.name_game.setText("Виселица")
            self.lang_button.setText("Сменить\n"
                                     "язык")
            self.setWindowTitle("Виселица")

        else:
            self.start_button.setText(translator.translate_start["СТАРТ"])
            self.name_game.setText(translator.translate_start["Виселица"])
            self.lang_button.setText(translator.translate_start["Сменить\n"
                                                     "язык"])
            self.setWindowTitle(translator.translate_start["Виселица"])


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
