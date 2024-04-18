from PyQt6.QtGui import QPixmap
from PyQt6.QtMultimedia import *
from PyQt6.QtCore import QUrl


class Settings():
    def __init__(self):
        self.sound_effect = QSoundEffect()

    # Звук нажатия на кнопку
    def sound_button(self):
        self.sound_effect.setSource(
            QUrl.fromLocalFile("src/sounds/system/buttons.wav"))
        self.sound_effect.play()

    # Загрузка изображения
    def load_image(self):
        pixmap = QPixmap(self.image_paths[self.lang_index])
        self.label_flag.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

    # Звук проигрыша
    def sound_game_over(self):
        self.sound_effect.setSource(QUrl.fromLocalFile(
            "src/sounds/system/game_over.wav"))
        self.sound_effect.play()

    # Звук выигрыша
    def sound_game_win(self):
        self.sound_effect.setSource(
            QUrl.fromLocalFile("src/sounds/system/game_win.wav"))
        self.sound_effect.play()

    # Обработчик изменения языка
    def change_lang(self):
        self.sound_button()
        if self.lang_index == 0:
            self.lang_index = 1
            self.label_mode.setText("RU-EN")
        else:
            self.lang_index = 0
            self.label_mode.setText("EN-RU")

    # Озвучивание слова
    def sound_words(self):
        self.sound_effect.setSource(QUrl.fromLocalFile(
            f"src/sounds/words/{self.word_shown}.mp3"))
        self.sound_effect.play()

    #
    def get_words(self):
        categories = {}
        with open('./src/config/dictionary.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            current_category = None
            for line in lines:
                if line.strip(): 
                    if not current_category:
                        current_category = line.strip()
                        categories[current_category] = []
                    else:
                        splt = line.strip().split("-")
                        categories[current_category].append((splt[0], splt[1]))
                else: 
                    current_category = None
        return categories
