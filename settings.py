from PyQt6.QtGui import QPixmap
from PyQt6.QtMultimedia import *
from PyQt6.QtCore import QUrl, QThread, pyqtSignal
from PyQt6.QtWidgets import QMessageBox

import requests, os
from dotenv import load_dotenv

# Рабочий поток, для запросов к серверу
class DownloadThread(QThread):
    finished = pyqtSignal(bool)

    def __init__(self, url, querystring, word_shown):
        super().__init__()
        self.url = url
        self.querystring = querystring
        self.payload = {
            "src": {word_shown},
            "hl": "en-us",
            "r": "-2",
            "v": "John",
            "c": "wav",
            "f": "48khz_8bit_stereo"
        }
        self.headers = {
            "content-type": "application/x-www-form-urlencoded",
            "X-RapidAPI-Key": "f5a8740e35msh8878ed03198b554p1caabejsnaddf4cf093a5",
            "X-RapidAPI-Host": "voicerss-text-to-speech.p.rapidapi.com"
        }
        
    def run(self):
        try: 
            response = requests.post(
                self.url, data=self.payload, headers=self.headers, params=self.querystring)
            if response.status_code == 200:
                with open("./src/sounds/temp/temp_word.wav", "wb") as file:
                    file.write(response.content)
                self.net_connect_flag = True
            else:
                self.net_connect_flag = False
        except:
            self.net_connect_flag = False

        self.finished.emit(self.net_connect_flag)


class Settings():
    def __init__(self):
        self.sound_effect = QSoundEffect()
        load_dotenv("./config/.env")
        api_key = os.getenv("API_KEY")
        self.url = "https://voicerss-text-to-speech.p.rapidapi.com/"
        self.querystring = {"key": api_key}        

    # Звук нажатия на кнопку
    def sound_button(self):
        self.sound_effect.setSource(
            QUrl.fromLocalFile("src/sounds/system/buttons.wav"))
        self.sound_effect.play()

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
        self.download_thread = DownloadThread(self.url, self.querystring, self.word_shown)
        self.download_thread.finished.connect(self.on_download_finished) # Назначение функции после выполенения действий в рабочем потоке
        self.download_thread.start() # Запуск рабочего потока для загрузки озвученного слова

    # Сбор слов из dictionary.txt
    def get_words(self):
        categories = {}
        with open('./config/dictionary.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            current_category = None
            for line in lines:
                if line.strip():
                    if not current_category:
                        current_category = line.strip()
                        categories[current_category] = []
                    else:
                        splt = line.strip().split(":")
                        categories[current_category].append((splt[0], splt[1]))
                else:
                    current_category = None
        return categories

    # Функция воспроизведения слова, после его загрузки
    def on_download_finished(self, success):
        if success:
            self.sound_effect.setSource(QUrl.fromLocalFile(
                "./src/sounds/temp/temp_word.wav"))
            self.sound_effect.play()
        else:
            info_message = QMessageBox()
            info_message.setIcon(QMessageBox.Icon.Information)
            info_message.setText("Проверьте подключение к Интернету")
            info_message.setWindowTitle("Нет подключения к сети")
            info_message.setStandardButtons(QMessageBox.StandardButton.Ok)
            info_message.exec()

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