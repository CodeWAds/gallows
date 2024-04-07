from PyQt6.QtGui import QPixmap
from PyQt6.QtMultimedia import *
from PyQt6.QtCore import QUrl, QTimer

# ПЕРЕДЕЛАТЬ СЛОВАРЬ НА ТЕКСТОВЫЙ ФАЙЛ! СМ. ТЗ
class Settings():
    def __init__(self):
        self.sound_effect = QSoundEffect()

    # Звук нажатия на кнопку
    def sound_button(self):
        self.sound_effect.setSource(QUrl.fromLocalFile("src/sounds/system/buttons.wav"))
        self.sound_effect.play()

    # Загрузка изображения
    def load_image(self):
        pixmap = QPixmap(self.image_paths[self.lang_index])
        self.label_flag.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

    # Звук проигрыша
    def sound_game_over(self):
        self.sound_effect.setSource(QUrl.fromLocalFile("src/sounds/system/game_over.wav"))
        self.sound_effect.play()

    # Звук выигрыша
    def sound_game_win(self):
        self.sound_effect.setSource(QUrl.fromLocalFile("src/sounds/system/game_win.wav"))
        self.sound_effect.play()

    # Обработчик изменения языка
    def change_lang(self):
        
        self.lang_index = (
            self.lang_index + 1) % len(self.image_paths)
        self.load_image()
        if self.lang_index == 0:
            self.start_button.setText("СТАРТ")
            self.name_game.setText("Виселица")
            self.lang_button.setText("Сменить\n"
                                     "язык")

        else:
            self.start_button.setText("START")
            self.name_game.setText("Hangman")
            self.lang_button.setText("Switch\n"
                                     "language")

    def sound_words(self):
        self.sound_effect.setSource(QUrl.fromLocalFile(f"src/sounds/words/{self.word_shown}.mp3"))
        self.sound_effect.play()
