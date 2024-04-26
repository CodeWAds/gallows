from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QStackedWidget, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QDialog, QGridLayout
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6 import QtCore, QtGui
from PyQt6.QtMultimedia import *
from settings import Settings
from generation_words import GenerationWords


import sys

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


class StartWindow(QWidget, Settings):
    def __init__(self):
        super().__init__()
        self.start_menu()

    def start_menu(self):
        
        self.lang_index = 0

        self.verticalLayout_4 = QVBoxLayout(self)
        self.horizontalLayout = QHBoxLayout()
        self.verticalLayout_5 = QVBoxLayout()

        # Текущий режим игры
        self.label_mode = QLabel(self)
        self.label_mode.setText("EN-RU")
        # self.label_mode.setGeometry(20, 10, 50, 30)
        self.label_mode.setObjectName("label_mode")
        self.label_mode.setStyleSheet("font-size: 10px;")
        self.verticalLayout_5.addWidget(self.label_mode)

        self.lang_button = QPushButton(self)
        # self.lang_button.setGeometry(10, 40, 70, 30)
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
        self.verticalLayout_5.addWidget(self.lang_button)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.lang_button.clicked.connect(self.change_lang)

        spacerItem = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.verticalLayout =QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.name_game = QLabel(self)
        self.name_game.setStyleSheet("font-size: 50px;")
        self.name_game.setObjectName("name_game")
        self.name_game.setText("Виселица")
        self.name_game.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.name_game)

        spacerItem3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_3 = QHBoxLayout()
        spacerItem4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)

        self.start_button = QPushButton(self)
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy)
        self.start_button.setMinimumSize(QtCore.QSize(160, 40))
        self.start_button.setObjectName("start_button")
        self.start_button.setText("СТАРТ")
        
        self.horizontalLayout_3.addWidget(self.start_button)
        self.start_button.clicked.connect(self.show_category_window)

        spacerItem5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        spacerItem6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        spacerItem7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)

    def show_category_window(self):
        category_widget = CategoryWindow(lang_index=self.lang_index)
        set_current(category_widget)


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
                                      "padding: 5px;\n"
                                      "font: 14px \"Comic Sans MS\";}\n"
                                      "QPushButton:hover { background-color:#8c7ae6; }"
                                      "")
            self.grid_buttons.addWidget(self.button, row, column, 1, 1)
            self.button.clicked.connect(
                lambda _, name_categ=name_categ: self.category_select(name_categ))

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

    def category_select(self, name_categ):
        game_window = GameWindow(
            category_words=name_categ, lang_index=self.lang_index)
        set_current(game_window)
        

# Окно с игрой
class GameWindow(QDialog, Settings, GenerationWords):
    def __init__(self, category_words, lang_index):
        super().__init__()
        self.category_words = category_words
        self.lang_index = lang_index
        self.attempts_left = -1
        self.data = self.get_words()
        self.generate_open_word()
        self.generate_hidden_word()
        self.game()

    # Создание окна игры, в соответствие с категорией
    def game(self):
        self.sound_button()
        
        self.verticalLayout = QVBoxLayout(self)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.horizontalLayout = QHBoxLayout()
        spacerItem1 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.gallows_picture = QLabel(self)
        self.gallows_picture.setPixmap(QPixmap("src/img/stages_gallows/stage_0.png"))
        self.gallows_picture.setScaledContents(True)

        self.horizontalLayout.addWidget(self.gallows_picture)
     
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        spacerItem4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_2 = QVBoxLayout()

        # Слово, показываемое игроку
        if self.lang_index == 0:
            self.open_word = QPushButton(self)
            self.open_word.setCursor(QtGui.QCursor(
                QtCore.Qt.CursorShape.PointingHandCursor))
            self.open_word.setFlat(True)
            pixmap = QPixmap("src/img/sound_word.png")
            icon = QIcon(pixmap)
            self.open_word.setIcon(icon)
            self.open_word.setIconSize(pixmap.size())
            self.open_word.setStyleSheet("background-color: transparent")
            
            self.open_word.clicked.connect(self.sound_words)
        else:
            self.open_word = QLabel(self)
            self.open_word.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.open_word.setStyleSheet("font-size: 17pt;")
            self.open_word.setText(" ".join(self._word_shown))
            self.open_word.setObjectName("open_word")

        self.verticalLayout_2.addWidget(self.open_word)

        # Слово, которое нужно отгадать
        self.hidden_word = QLabel(self)
        self.hidden_word.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hidden_word.setStyleSheet("font-size: 13pt;")
        self.hidden_word.setText(" ".join(self.word_hide))
        self.hidden_word.setObjectName("hidden_word")
        self.verticalLayout_2.addWidget(self.hidden_word)

        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        spacerItem6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem7)

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

        for row in keyboard:
            key_row = QHBoxLayout()
            for key in row:
                button_keyboard = QPushButton(key)
                key_row.addWidget(button_keyboard)
                button_keyboard.setStyleSheet("QPushButton{border: 1px solid #dfe6e9;\n"
                                              "background-color: #a29bfe;\n"
                                              "padding: 10px;\n"
                                              "border-radius: 5px;\n"
                                              "font: 10pt \"Comic Sans MS\";}\n"
                                              "QPushButton:hover { background-color: #8c7ae6; }"
                                              "")
                button_keyboard.setCursor(QtGui.QCursor(
                    QtCore.Qt.CursorShape.PointingHandCursor))
                button_keyboard.clicked.connect(self.make_guess)

            self.verticalLayout.addLayout(key_row)
        spacerItem8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.make_guess()


    # Вызов дополнительного окна с результатом игры
    def show_popup(self, result_game):

        self.popup_game = QDialog(self)
        self.verticalLayout = QVBoxLayout(self.popup_game)
        self.gridLayout = QGridLayout()

        if result_game == "win":
            image = "cat_win"
        else:
            image = "cat_over"

        if result_game == "win":
            title = "Победа!"
            text_popup = "Поздравляем! Вы выиграли!"
        else:
            title = "Поражение!"
            text_popup = f"""Увы! Вы проиграли!\nПравильный ответ: {self._word_hide}"""

        self.popup_game.setWindowTitle(title)
        self.popup_game.setWindowIcon(
            QIcon("src/img/stages_gallows/stage_6.png"))
        self.popup_game.setFixedSize(480, 150)

        label_image = QLabel(self.popup_game)
        label_image.setPixmap(QPixmap(f"src/img/{image}.png"))
        label_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(label_image, 1, 0, 1, 1)
        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)

        label_answer = QLabel(self.popup_game)
        label_answer.setStyleSheet("font-size: 15px")
        label_answer.setText(text_popup)
        label_answer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(label_answer, 1, 3, 1, 1)
        
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 4, 1, 1)
        spacerItem4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 5, 1, 1)
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 6, 1, 1)
        spacerItem11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem11, 1, 7, 1, 1)
    
        self.gridLayout.addWidget(label_answer, 1, 3, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        spacerItem5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)

        self.button_ok = QPushButton('Вернуться в меню')
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
        self.horizontalLayout.addWidget(self.button_ok)
        spacerItem6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.button_ok.clicked.connect(self.return_to_menu)
        self.popup_game.rejected.connect(self.return_to_menu)
        self.popup_game.exec()

    # Возврат в меню
    def return_to_menu(self):
        self.popup_game.deleteLater()
        start_widget = StartWindow()
        set_current(start_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    Stack = QStackedWidget()
    start = StartWindow()
    set_current(start)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
