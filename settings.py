from PyQt6.QtGui import QPixmap
from PyQt6.QtMultimedia import *
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QMessageBox

import requests
import os
from dotenv import load_dotenv


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
        self.download_words()
        if self.net_connect_flag:
            self.sound_effect.setSource(QUrl.fromLocalFile(
                f"./src/sounds/temp/temp_word.wav"))
            self.sound_effect.play()

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
                        splt = line.strip().split("-")
                        categories[current_category].append((splt[0], splt[1]))
                else:
                    current_category = None
        return categories
    
    def download_words(self):
        self.payload = {
            "src": {self.word_shown},
            "hl": "en-us",
            "r": "0",
            "v": "John",
            "c": "wav",
            "f": "48khz_8bit_stereo"
        }
        self.headers = {
            "content-type": "application/x-www-form-urlencoded",
            "X-RapidAPI-Key": "f5a8740e35msh8878ed03198b554p1caabejsnaddf4cf093a5",
            "X-RapidAPI-Host": "voicerss-text-to-speech.p.rapidapi.com"
        }
        try:
            self.response = requests.post(
                self.url, data=self.payload, headers=self.headers, params=self.querystring)

            if self.response.status_code == 200:
                with open("./src/sounds/temp/temp_word.wav", "wb") as file:
                    file.write(self.response.content)
                print("File saved successfully")
                self.net_connect_flag = True
            else:
                pass
        except:
            info_message = QMessageBox()
            info_message.setIcon(QMessageBox.Icon.Information)
            info_message.setText("Проверьте подключение к Интернету")
            info_message.setWindowTitle("Нет подключения к сети")
            info_message.setStandardButtons(QMessageBox.StandardButton.Ok)
            info_message.exec()
            self.net_connect_flag = False

