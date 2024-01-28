from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QStackedLayout, QHBoxLayout, QDialog,  QMessageBox
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
        self.lang_index = 0
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

        ai_button = QPushButton(self.category_widget)

        ai_button.setGeometry(QtCore.QRect(140, 310, 147, 39))
        ai_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        ai_button.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        ai_button.setAutoFillBackground(False)
        ai_button.setStyleSheet("QPushButton{border: 1px solid #dfe6e9;\n"
                                "background-color: #a29bfe;\n"
                                "border-radius: 5px;\n"
                                "font: 10pt \"Comic Sans MS\";}\n"
                                "QPushButton:hover { background-color: #8c7ae6; }"
                                "")
        ai_button.setObjectName("ai_button")
        ai_button.setText("Искусственный\n"
                          "интеллект")
        ai_button.clicked.connect(self.ai)

        design_button = QPushButton(self.category_widget)

        design_button.setGeometry(QtCore.QRect(292, 310, 147, 39))
        design_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        design_button.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        design_button.setAutoFillBackground(False)
        design_button.setStyleSheet("QPushButton{border: 1px solid #dfe6e9;\n"
                                    "background-color: #a29bfe;\n"
                                    "border-radius: 5px;\n"
                                    "font: 10pt \"Comic Sans MS\";}\n"
                                    "QPushButton:hover { background-color: #8c7ae6; }"
                                    "")
        design_button.setObjectName("design_button")
        design_button.setText("Дизайн")
        design_button.clicked.connect(self.design)

        cybersecurity_button = QPushButton(self.category_widget)

        cybersecurity_button.setGeometry(QtCore.QRect(444, 310, 147, 39))
        cybersecurity_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        cybersecurity_button.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        cybersecurity_button.setAutoFillBackground(False)
        cybersecurity_button.setStyleSheet("QPushButton{border: 1px solid #dfe6e9;\n"
                                           "background-color: #a29bfe;\n"
                                           "border-radius: 5px;\n"
                                           "font: 10pt \"Comic Sans MS\";}\n"
                                           "QPushButton:hover { background-color: #8c7ae6; }"
                                           "")
        cybersecurity_button.setObjectName("cybersecurity_button")
        cybersecurity_button.setText("Кибербезопасность")
        cybersecurity_button.clicked.connect(self.cybersecurity)

        self.setCentralWidget(self.category_widget)

        if self.lang_index != 0:
            name_category.setText("Category")
            hardware_button.setText("Hardware")
            software_button.setText("Software")
            internet_button.setText("Internet")
            ai_button.setText("Artificial\n"
                              "Intelligence")
            design_button.setText("Design")
            cybersecurity_button.setText("Cybersecurity")

    def hardware(self):
        self.sound_button()
        self.hardware_widget = QWidget(self)
        self.hardware_widget.setObjectName("hardware_widget")
        self.category_words = 1
        self.generate_open_word()
        self.generate_hidden_word()
        self.game(self.hardware_widget)

        self.setCentralWidget(self.hardware_widget)

    def software(self):
        self.sound_button()
        self.software_widget = QWidget(self)
        self.software_widget.setObjectName("software_widget")
        self.category_words = 2
        self.generate_open_word()
        self.generate_hidden_word()
        self.game(self.software_widget)

        self.setCentralWidget(self.software_widget)

    def internet(self):
        self.sound_button()
        self.internet_widget = QWidget(self)
        self.internet_widget.setObjectName("internet_widget")
        self.category_words = 3
        self.generate_open_word()
        self.generate_hidden_word()
        self.game(self.internet_widget)

        self.setCentralWidget(self.internet_widget)

    def ai(self):
        self.sound_button()
        self.ai_widget = QWidget(self)
        self.ai_widget.setObjectName("ai_widget")
        self.category_words = 4
        self.generate_open_word()
        self.generate_hidden_word()
        self.game(self.ai_widget)

        self.setCentralWidget(self.ai_widget)

    def design(self):
        self.sound_button()
        self.design_widget = QWidget(self)
        self.design_widget.setObjectName("design_widget")
        self.category_words = 5
        self.generate_open_word()
        self.generate_hidden_word()
        self.game(self.design_widget)

        self.setCentralWidget(self.design_widget)

    def cybersecurity(self):
        self.sound_button()
        self.cybersecurity_widget = QWidget(self)
        self.cybersecurity_widget.setObjectName("cybersecurity_widget")
        self.category_words = 6
        self.generate_open_word()
        self.generate_hidden_word()
        self.game(self.cybersecurity_widget)

        self.setCentralWidget(self.cybersecurity_widget)

    def game(self, widget):
        self.widget = widget
        self.attempts_left = -1
        self.gallows_picture = QLabel(widget)
        self.gallows_picture.setGeometry(QtCore.QRect(10, 10, 301, 281))
        pixmap_gallow = QPixmap("src/stages_with_bg/stage_0.png")
        self.gallows_picture.setPixmap(pixmap_gallow)
        self.resize(pixmap_gallow.width(), pixmap_gallow.height())
        self.gallows_picture.setObjectName("gallow_picture")

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

        if self.lang_index == 0:
            keyboard = russian_keys
        else:
            keyboard = english_keys
        self.label_keyboard = QLabel(widget)
        self.label_keyboard.setGeometry(QtCore.QRect(10, 316, 701, 151))
        self.keyboard_layout = QVBoxLayout(self.label_keyboard)

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
                button_keyboard.clicked.connect(self.make_guess)

            self.keyboard_layout.addLayout(key_row)
        self.label_keyboard.setObjectName("label_keyboard")
        open_word = QLabel(widget)
        open_word.setGeometry(QtCore.QRect(320, 20, 391, 121))
        open_word.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        open_word.setStyleSheet("font-size: 17pt;")
        open_word.setText(self.word_shown)
        open_word.setObjectName("open_word")

        self.hidden_word = QLabel(widget)
        self.hidden_word.setGeometry(QtCore.QRect(320, 160, 391, 121))
        self.hidden_word.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hidden_word.setStyleSheet("font-size: 13pt;")
        self.hidden_word.setText(" ".join(self.word_hide))
        self.hidden_word.setObjectName("hidden_word")
        self.make_guess()

    def sound_button(self):
        self.sender().setEnabled(False)
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        self.player.setSource(QUrl.fromLocalFile("src/sounds/buttons.wav"))
        self.audioOutput.setVolume(50)
        self.player.play()
        
        self.sender().setEnabled(True)

    def sound_game_over(self):
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        self.player.setSource(QUrl.fromLocalFile("src/sounds/game_over.wav"))
        self.audioOutput.setVolume(50)
        self.player.play()

    def sound_game_win(self):
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        self.player.setSource(QUrl.fromLocalFile("src/sounds/game_win.wav"))
        self.audioOutput.setVolume(50)
        self.player.play()

    def show_popup(self, result_game):
        self.popup_game = QDialog(self)
        if result_game == "win":
            image = "cat_win"
        else:
            image = "cat_over"

        if self.lang_index == 0:
            return_button = "Вернуться в меню"
            if result_game == "win":
                title = "Победа!"
                text_popup = "Поздравляем! Вы выиграли!"
            else:
                title = "Поражение!"
                text_popup = f"""Увы! Вы проиграли!\n
                    Правильный ответ: {self._word_hide}"""
        else:
            return_button = "Return to menu"
            if result_game == "win":
                title = "Win"
                text_popup = "You won!"
            else:
                title = "Lose"
                text_popup = f"""You lose!\n
                Correct answer: {self._word_hide}"""

        self.popup_game.setWindowTitle(title)
        self.popup_game.setWindowIcon(QIcon("src/stages_with_bg/stage_6.png"))
        self.popup_game.setFixedSize(480, 150)

        label_answer = QLabel(self.popup_game)
        label_answer.setGeometry(QtCore.QRect(0, 10, 480, 60))
        label_answer.setStyleSheet("font-size: 10pt")
        label_answer.setText(text_popup)
        label_answer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        label_text = QLabel(self.popup_game)
        label_text.setGeometry(QtCore.QRect(180, 100, 480, 50))

        pixmap = QPixmap(f"src/{image}.png")
        label_image = QLabel(self.popup_game)
        label_image.setGeometry(QtCore.QRect(20, 30, 60, 60))
        label_image.setPixmap(pixmap)
        label_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.button_ok = QPushButton('Вернуться в меню', label_text)
        self.button_ok.setStyleSheet("QPushButton{border: 1px solid #dfe6e9;\n"
                                "background-color: #a29bfe;\n"
                                "padding: 5px;\n"
                                "border-radius: 5px;\n"
                                "font: 10pt \"Comic Sans MS\";}\n"
                                "QPushButton:hover { background-color: #8c7ae6; }"
                                "")
        self.button_ok.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        if self.lang_index != 0:
            self.button_ok.setText(return_button)
        self.button_ok.clicked.connect(self.return_to_menu)
        self.popup_game.exec()

    def return_to_menu(self):
        self.popup_game.hide()
        self.widget.hide()

    def generate_open_word(self):
        if self.category_words == 1:
            _words = translator.words_hardware
        elif self.category_words == 2:
            _words = translator.words_software
        elif self.category_words == 3:
            _words = translator.words_internet
        elif self.category_words == 4:
            _words = translator.words_ai
        elif self.category_words == 5:
            _words = translator.words_design
        else:
            _words = translator.words_cybersecurity
        self.word_of_items = list(_words.items())
        self.random_index = random.randint(0, len(_words)-1)
        self.word_shown = self.word_of_items[self.random_index][self.lang_index]

    def generate_hidden_word(self):
        self._word_hide = self.word_of_items[self.random_index][self.lang_index-1]
        self.word_hide = []
        for i in self._word_hide:
            if i == " ":
                self.word_hide.append("\n")
            elif i == "-":
                self.word_hide.append("-")
            else:
                self.word_hide.append("_")

    def make_guess(self):
        self.sound_button()
        sender = self.sender()
        self.guess = sender.text()
        self.guess_letter = self.guess.lower()
        sender.setEnabled(False)

        if self.guess_letter in self._word_hide:
            for i, letter in enumerate(self._word_hide):
                if letter == self.guess_letter:
                    self.word_hide[i] = self.guess_letter
            self.hidden_word.setText(" ".join(self.word_hide))
        else:
            self.attempts_left += 1
            pixmap_gallow = QPixmap(
                f"src/stages_with_bg/stage_{self.attempts_left}.png")
            self.gallows_picture.setPixmap(pixmap_gallow)
        if "_" not in self.word_hide:
            self.sound_game_win()
            self.result_game = "win"
            self.show_popup(self.result_game)
        elif self.attempts_left == 6:
            self.sound_game_over()
            self.result_game = "over"
            self.show_popup(self.result_game)

    def load_image(self):
        pixmap = QPixmap(self.image_paths[self.lang_index])
        self.label_flag.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

    def change_lang(self):
        self.sound_button()
        self.lang_index = (
            self.lang_index + 1) % len(self.image_paths)
        self.load_image()
        if self.lang_index == 0:
            self.start_button.setText("СТАРТ")
            self.name_game.setText("Виселица")
            self.lang_button.setText("Сменить\n"
                                     "язык")
            self.setWindowTitle("Виселица")

        else:
            self.start_button.setText("START")
            self.name_game.setText("Gallows")
            self.lang_button.setText("Switch\n"
                                     "language")
            self.setWindowTitle("Gallows")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
