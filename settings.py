from PyQt6.QtGui import QPixmap
from PyQt6.QtMultimedia import *
from PyQt6.QtCore import QUrl, QTimer
from PyQt6 import QtCore

# ПЕРЕДЕЛАТЬ СЛОВАРЬ НА ТЕКСТОВЫЙ ФАЙЛ! СМ. ТЗ
class Settings():

    def playSound(self):
         if self.mus == False:
            self.mus = True
            # Создаем объект звукового эффекта и загружаем в него аудиофайл
            sound_effect = QSoundEffect()
            sound_effect.setSource(QUrl.fromLocalFile('src/sounds/system/buttons.wav')) # Замените 'click_sound.wav' на путь к вашему аудиофайлу
            sound_effect.setVolume(1) # Устанавливаем громкость звука
            sound_effect.play()

    # Загрузка изображения
    def load_image(self):
        pixmap = QPixmap(self.image_paths[self.lang_index])
        self.label_flag.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

    # Базовый звук, для кнопок
    def sound_button_lang(self):
        if self.mus == False:
            self.mus = True
            sender = self.sender()
            sender.setEnabled(False)
            self.player = QMediaPlayer()
            self.audioOutput = QAudioOutput()
            self.player.setAudioOutput(self.audioOutput)
            self.player.setSource(QUrl.fromLocalFile(
                "src/sounds/system/buttons.wav"))
            self.audioOutput.setVolume(50)
            self.player.play()
            timer = QTimer(self)
            timer.singleShot(500, self.enable_button)
        self.mus = False

    def enable_button(self):
        self.lang_button.setEnabled(True)

    def sound_button(self):
        if self.mus == False:
            self.mus = True
            sender = self.sender()
            sender.setEnabled(False)
            self.player = QMediaPlayer()
            self.audioOutput = QAudioOutput()
            self.player.setAudioOutput(self.audioOutput)
            self.player.setSource(QUrl.fromLocalFile(
                "src/sounds/system/buttons.wav"))
            self.audioOutput.setVolume(50)
            self.player.play()
        self.mus = False

    # Звук проигрыша

    def sound_game_over(self):
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        self.player.setSource(QUrl.fromLocalFile(
            "src/sounds/system/game_over.mp3"))
        self.audioOutput.setVolume(50)
        self.player.play()

    # Звук выигрыша
    def sound_game_win(self):
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        self.player.setSource(QUrl.fromLocalFile(
            "src/sounds/system/game_win.mp3"))
        self.audioOutput.setVolume(50)
        self.player.play()

    # Обработчик изменения языка
    def change_lang(self):
        self.sound_button_lang()
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
        self.mus = True
        sender = self.sender()
        sender.setEnabled(False)
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput)
        self.player.setSource(QUrl.fromLocalFile(
            f"src/sounds/words/{self.word_shown}.mp3"))
        self.audioOutput.setVolume(50)
        self.player.play()
        timer = QTimer(self)
        timer.singleShot(3000, self.enable_words)

    def enable_words(self):
        self.mus = False
        self.sound_word.setEnabled(True)
