from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QStackedWidget, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QDialog, QGridLayout
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6 import QtCore, QtGui
from PyQt6.QtMultimedia import *
from settings import Settings
from generation_words import GenerationWords


import sys, asyncio

#  Установка виджета
def set_current(new_widget):
    previous_widget = Stack.currentWidget()
    if previous_widget:
        previous_widget.deleteLater()

    Stack.addWidget(new_widget)

    Stack.setCurrentWidget(new_widget)

#  Главное окно
class MainWindow(QMainWindow, Settings):
    def __init__(self):
        super().__init__()
        self.create_window()

    def create_window(self):
        self.setObjectName("MainWindow")
        self.setMinimumSize(720, 480)
        self.setStyleSheet("background-color: rgb(140, 83, 255);\n"
                           "font: 14pt \"Comic Sans MS\"")
        self.setCentralWidget(Stack)
        icon = QIcon("src/img/stages_gallows/stage_6.png")
        self.setWindowIcon(icon)
        self.setWindowTitle("Виселица")


class StartWindow(QStackedWidget, Settings):
    def __init__(self):
        super().__init__()
        self.start_menu()

    def start_menu(self):

        # Текущий режим игры
        self.label_mode = QLabel("EN-RU", self)
        self.label_mode.setGeometry(20, 10, 50, 30)
        self.lang_index = 0
        self.label_mode.setObjectName("label_mode")
        self.label_mode.setStyleSheet("font-size: 10pt;")

        self.name_game = QLabel(self)
        self.name_game.setStyleSheet("font-size: 25pt;")
        self.name_game.setObjectName("name_game")
        self.name_game.setText("Виселица")
        self.name_game.setGeometry(280, 100, 160, 50)
        self.name_game.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.lang_button = QPushButton(self)
        self.lang_button.setGeometry(10, 40, 70, 30)
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
                                 "режим")
        self.lang_button.clicked.connect(self.change_lang)

        self.start_button = QPushButton(self)
        self.start_button.setGeometry(280, 260, 160, 40)
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

    def adjust_widget_sizes(self):

        label_width = self.width() // 2
        label_height = self.height() // 2

        # Центрируем название игры относительно новых размеров окна
        label_x = (self.width() - label_width) // 2
        label_y = (self.height() - label_height) // 2 - 100

        self.name_game.setGeometry(label_x, label_y, label_width, label_height)

        # Обновляем размеры и положение кнопки "СТАРТ"
        button_width = label_width
        button_height = 40
        button_x = label_x
        button_y = label_y + label_height + 20

        self.start_button.setGeometry(
            button_x, button_y, button_width, button_height)

        # Устанавливаем размер текста пропорционально высоте виджета
        font_size = label_height * 0.1
        self.name_game.setStyleSheet(f"font-size: {font_size}pt;")

    def show_category_window(self):
        category_widget = CategoryWindow(lang_index=self.lang_index)
        set_current(category_widget)

    def resizeEvent(self, event):
        self.adjust_widget_sizes()

        super().resizeEvent(event)


# Окно Категорий
class CategoryWindow(QWidget, Settings):
    def __init__(self, lang_index):
        super().__init__()
        self.lang_index = lang_index
        self.category_game()

    def category_game(self):
        self.sound_button()
        self.sender().setEnabled(True)

        self.page_layout = QVBoxLayout(self)
        spacerItem = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.page_layout.addItem(spacerItem)

        self.name_menu_category = QLabel(self)
        self.name_menu_category.setStyleSheet("font-size: 50px;")
        self.name_menu_category.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_menu_category.setObjectName("name_game")
        self.name_menu_category.setText("Категория")
        self.page_layout.addWidget(self.name_menu_category)

        self.grid_buttons = QGridLayout()

        self.data = self.get_words()
        row = 1
        column = 0
        # Генерация кнопок с названиями категорий
        for name_categ in self.data:
            if column > 2:
                row += 1
                column = 1
            else:
                column += 1

            self.button = QPushButton(self)
            sizePolicy = QSizePolicy(
                QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(
                self.button.sizePolicy().hasHeightForWidth())
            self.button.setSizePolicy(sizePolicy)
            self.button.setMinimumSize(QtCore.QSize(160, 50))
            self.button.setText(f"{name_categ}")
            self.button.setCursor(QtGui.QCursor(
                QtCore.Qt.CursorShape.PointingHandCursor))
            self.button.setStyleSheet("QPushButton{border: 1px solid #dfe6e9;\n"
                                      "background-color: #a29bfe;\n"
                                      "border-radius: 5px;\n"
                                      "font: 14px \"Comic Sans MS\";}\n"
                                      "QPushButton:hover { background-color:#8c7ae6; }"
                                      "")
            self.grid_buttons.addWidget(self.button, row, column, 1, 1)
            self.button.clicked.connect(
                lambda _, name_categ=name_categ: self.category_selected(name_categ))

        spacerItem1 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.grid_buttons.addItem(spacerItem1, 1, 4, 1, 1)

        spacerItem2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.grid_buttons.addItem(spacerItem2, 1, 0, 1, 1)

        spacerItem3 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.grid_buttons.addItem(spacerItem3, row+1, 2, 1, 1)

        spacerItem4 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.page_layout.addItem(spacerItem4)
        self.page_layout.addLayout(self.grid_buttons)

    def category_selected(self, name_categ):
        game_window = GameWindow(
            category_words=name_categ, lang_index=self.lang_index)
        set_current(game_window)

    # def adjust_widget_sizes(self):
    #     label_width = self.width() // 2
    #     label_height = self.height() // 2

    #     # Центрирование названия категории относительно новых размеров окна
    #     label_x = (self.width() - label_width) // 2
    #     label_y = (self.height() - label_height) // 2 - 100

    #     self.name_menu_category.setGeometry(
    #         label_x, label_y, label_width, label_height)

    #     font_size = label_height * 0.1
    #     self.name_menu_category.setStyleSheet(f"font-size: {font_size}pt;")

    #     # Рассчёт размеров и положения кнопок категорий
    #     button_width = label_width // 3 + 5
    #     button_height = 39
    #     button_spacing = 10
    #     buttons_per_row = 3

    #     button_x = label_x
    #     button_y = label_y + label_height + 20

    #     for i, button in enumerate([self.hardware_button, self.software_button, self.internet_button, self.ai_button, self.design_button, self.cybersecurity_button]):
    #         button.setGeometry(button_x, button_y, button_width, button_height)

    #         if (i + 1) % buttons_per_row == 0:
    #             button_x = label_x
    #             button_y += button_height + button_spacing
    #         else:
    #             button_x += button_width + button_spacing

    # def resizeEvent(self, event):
    #     self.adjust_widget_sizes()
    #     super().resizeEvent(event)


# Окно с игрой
class GameWindow(QDialog, Settings, GenerationWords):
    def __init__(self, category_words, lang_index):
        super().__init__()
        self.category_words = category_words
        self.lang_index = lang_index
        self.data = self.get_words()
        self.generate_open_word()
        self.generate_hidden_word()
        self.game()

    # Создание окна игры, в соответствие с категорией
    def game(self):
        self.sound_button()
        self.attempts_left = -1
        self.gallows_picture = QLabel(self)
        self.gallows_picture.setGeometry(10, 10, 301, 281)
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
        self.label_keyboard = QLabel(self)
        self.label_keyboard.setGeometry(10, 316, 701, 151)
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
        open_word = QLabel(self)
        open_word.setGeometry(320, 20, 391, 121)
        open_word.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        open_word.setStyleSheet("font-size: 17pt;")
        open_word.setText(" ".join(self._word_shown))
        open_word.setObjectName("open_word")

        # Слово, которое нужно отгадать
        self.hidden_word = QLabel(self)
        self.hidden_word.setGeometry(320, 160, 391, 121)
        self.hidden_word.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hidden_word.setStyleSheet("font-size: 13pt;")
        self.hidden_word.setText(" ".join(self.word_hide))
        self.hidden_word.setObjectName("hidden_word")
        self.make_guess()

        if self.lang_index == 0:
            self.sound_word = QPushButton(self)
            self.sound_word.setGeometry(665, 20, 48, 48)

            self.sound_word.setCursor(QtGui.QCursor(
                QtCore.Qt.CursorShape.PointingHandCursor))
            self.sound_word.setFlat(True)
            pixmap = QPixmap("src/img/sound_word.png")
            icon = QIcon(pixmap)
            self.sound_word.setIcon(icon)
            self.sound_word.setIconSize(pixmap.size())
            self.sound_word.setStyleSheet("background-color: transparent")
            
            self.sound_word.clicked.connect(self.sound_words)

    def adjust_widget_sizes(self):
        label_width = self.width() // 2
        label_height = self.height() // 2

    def resizeEvent(self, event):
        self.adjust_widget_sizes()
        super().resizeEvent(event)

    # Вызов дополнительного окна с результатом игры
    def show_popup(self, result_game):

        self.popup_game = QDialog(self)

        if result_game == "win":
            image = "cat_win"
        else:
            image = "cat_over"

        if result_game == "win":
            title = "Победа!"
            text_popup = "Поздравляем! Вы выиграли!"
        else:
            title = "Поражение!"
            text_popup = f"""Увы! Вы проиграли!\n
                Правильный ответ: {self._word_hide}"""

        self.popup_layout = QHBoxLayout(self.popup_game)
        self.popup_game.setWindowTitle(title)
        self.popup_game.setWindowIcon(
            QIcon("src/img/stages_gallows/stage_6.png"))
        self.popup_game.setFixedSize(480, 150)

        label_answer = QLabel(self.popup_game)
        label_answer.setGeometry(0, 10, 480, 60)
        label_answer.setStyleSheet("font-size: 10px")
        label_answer.setText(text_popup)
        label_answer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        label_text = QLabel(self.popup_game)
        label_text.setGeometry(180, 100, 480, 50)

        pixmap = QPixmap(f"src/img/{image}.png")
        label_image = QLabel(self.popup_game)
        label_image.setGeometry(20, 30, 60, 60)
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

        self.button_ok.setText("Вернуться в меню")
        self.button_ok.clicked.connect(self.return_to_menu)
        self.popup_game.rejected.connect(self.return_to_menu)
        self.popup_game.exec()

    # Возврат в меню
    def return_to_menu(self):
        self.popup_game.deleteLater()
        start_widget = StartWindow()
        set_current(start_widget)

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

    Stack = QStackedWidget()
    start = StartWindow()
    set_current(start)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
