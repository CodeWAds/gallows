from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QDialog, QToolButton
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6 import QtCore, QtGui
from PyQt6.QtMultimedia import *
from settings import Settings
from generation_words import Generation_words
from PyQt6.QtCore import Qt


import sys


#  Главного меню
class MainWindow(QMainWindow, Settings, Generation_words):
    def __init__(self):
        super().__init__()
        self.create_window()

    def create_window(self):
        self.setObjectName("MainWindow")
        self.setMinimumSize(720, 480)
        self.setStyleSheet("background-color: rgb(140, 83, 255);\n"
                           "font: 14pt \"Comic Sans MS\"")
        self.StartMenu()

    def StartMenu(self):
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        icon = QIcon("src/img/stages_gallows/stage_6.png")
        self.setWindowIcon(icon)

        # Установка изображения языка
        self.label_flag = QLabel(self)
        self.label_flag.setGeometry(QtCore.QRect(26, 10, 31, 31))
        self.image_paths = ['src/img/flag_rus.png', 'src/img/flag_en.png']
        self.lang_index = 0
        self.load_image()
        self.label_flag.setObjectName("label_flag")

        self.name_game = QLabel(self)
        self.name_game.setStyleSheet("font-size: 25pt;")
        self.name_game.setObjectName("name_game")
        self.name_game.setText("Виселица")
        self.name_game.setGeometry(QtCore.QRect(280, 100, 160, 50))
        self.name_game.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

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
        self.start_button.clicked.connect(self.show_category_window)

        self.setCentralWidget(self.centralwidget)

        self.setWindowTitle("Виселица")

    # Изменение окна

    def show_category_window(self):
        category_widget = CategoryWindow(lang_index=self.lang_index)
        self.setCentralWidget(category_widget)


# Окно Категорий
class CategoryWindow(MainWindow):
    def __init__(self, lang_index):
        super().__init__()
        self.lang_index = lang_index
        self.category_game()

    def category_game(self):
        self.sound_button()
        category_widget = QWidget(self)
        category_widget.setObjectName("category_widget")

        name_menu_category = QLabel(category_widget)
        name_menu_category.setGeometry(QtCore.QRect(280, 100, 160, 50))
        name_menu_category.setStyleSheet("font-size: 25pt;")
        name_menu_category.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        name_menu_category.setObjectName("name_game")
        name_menu_category.setText("Категория")

        hardware_button = QPushButton(category_widget)
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

        software_button = QPushButton(category_widget)

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

        internet_button = QPushButton(category_widget)

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

        ai_button = QPushButton(category_widget)

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

        design_button = QPushButton(category_widget)

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

        cybersecurity_button = QPushButton(category_widget)

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

        self.setCentralWidget(category_widget)

        if self.lang_index != 0:
            name_menu_category.setText("Category")
            hardware_button.setText("Hardware")
            software_button.setText("Software")
            internet_button.setText("Internet")
            ai_button.setText("Artificial\n"
                              "Intelligence")
            design_button.setText("Design")
            cybersecurity_button.setText("Cybersecurity")

    def hardware(self):
        self.sound_button()
        game_window = GameWindow(category_words=1, lang_index=self.lang_index)
        self.setCentralWidget(game_window)

    def software(self):
        self.sound_button()
        game_window = GameWindow(category_words=2, lang_index=self.lang_index)
        self.setCentralWidget(game_window)

    def internet(self):
        self.sound_button()
        game_window = GameWindow(category_words=3, lang_index=self.lang_index)
        self.setCentralWidget(game_window)

    def ai(self):
        self.sound_button()
        game_window = GameWindow(category_words=4, lang_index=self.lang_index)
        self.setCentralWidget(game_window)

    def design(self):
        self.sound_button()
        game_window = GameWindow(category_words=5, lang_index=self.lang_index)
        self.setCentralWidget(game_window)

    def cybersecurity(self):
        self.sound_button()
        game_window = GameWindow(category_words=6, lang_index=self.lang_index)
        self.setCentralWidget(game_window)


# Окно с игрой
class GameWindow(MainWindow):
    def __init__(self, category_words, lang_index):
        super().__init__()
        self.category_words = category_words
        self.lang_index = lang_index

        self.create_game_window()

    # Создание окна игры, в соответствие с категорией
    def create_game_window(self):
        self.sound_button()
        self.game_widget = QWidget(self)
        self.game_widget.setObjectName("game_widget")
        self.generate_open_word()
        self.generate_hidden_word()
        self.game(self.game_widget)

        self.setCentralWidget(self.game_widget)

    def game(self, widget):
        self.widget = widget
        self.attempts_left = -1
        self.gallows_picture = QLabel(widget)
        self.gallows_picture.setGeometry(QtCore.QRect(10, 10, 301, 281))
        pixmap_gallow = QPixmap("src/img/stages_gallows/stage_0.png")
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

        # Слово, показываемое игроку
        open_word = QLabel(widget)
        open_word.setGeometry(QtCore.QRect(320, 20, 391, 121))
        open_word.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        open_word.setStyleSheet("font-size: 17pt;")
        open_word.setText(" ".join(self._word_shown))
        open_word.setObjectName("open_word")

        # Слово, которое нужно отгадать
        self.hidden_word = QLabel(widget)
        self.hidden_word.setGeometry(QtCore.QRect(320, 160, 391, 121))
        self.hidden_word.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hidden_word.setStyleSheet("font-size: 13pt;")
        self.hidden_word.setText(" ".join(self.word_hide))
        self.hidden_word.setObjectName("hidden_word")
        self.make_guess()

        if self.lang_index == 0:
            self.sound_word = QPushButton(self)
            self.sound_word.setGeometry(670, 20, 48, 48)
            
            self.sound_word.setCursor(QtGui.QCursor(
                QtCore.Qt.CursorShape.PointingHandCursor))
            self.sound_word.setFlat(True)
            pixmap = QPixmap("src/img/sound_word.png")
            icon = QIcon(pixmap)
            self.sound_word.setIcon(icon)
            self.sound_word.setIconSize(pixmap.size())

            self.sound_word.clicked.connect(self.sound_words)

    # Вызов дополнительного окна с результатом игры

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
        self.popup_game.setWindowIcon(
            QIcon("src/img/stages_gallows/stage_6.png"))
        self.popup_game.setFixedSize(480, 150)

        label_answer = QLabel(self.popup_game)
        label_answer.setGeometry(QtCore.QRect(0, 10, 480, 60))
        label_answer.setStyleSheet("font-size: 10pt")
        label_answer.setText(text_popup)
        label_answer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        label_text = QLabel(self.popup_game)
        label_text.setGeometry(QtCore.QRect(180, 100, 480, 50))

        pixmap = QPixmap(f"src/img/{image}.png")
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

    # Возврат в меню
    def return_to_menu(self):
        self.popup_game.hide()
        main_window = MainWindow()
        self.setCentralWidget(main_window)

    # Обработка выбора кнопок на виртуальной клавиатуре
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
                f"src/img/stages_gallows/stage_{self.attempts_left}.png")
            self.gallows_picture.setPixmap(pixmap_gallow)
        if "_" not in self.word_hide:
            self.sound_game_win()
            self.result_game = "win"
            self.show_popup(self.result_game)
        elif self.attempts_left == 6:
            self.sound_game_over()
            self.result_game = "over"
            self.show_popup(self.result_game)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
