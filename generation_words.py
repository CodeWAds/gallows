from PyQt6.QtMultimedia import *
import random
import translator


class Generation_words():

    # Слово, показываемое игроку
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

        if self.lang_index == 0:
            self.word_shown = self.word_of_items[self.random_index][0]

        else:
            self.word_shown = self.word_of_items[self.random_index][1]


    # Слово, которое игрок долже отгадать
    def generate_hidden_word(self):
        if self.lang_index == 0:
            self._word_hide = self.word_of_items[self.random_index][1]
        else:
            self._word_hide = self.word_of_items[self.random_index][0]
        self.word_hide = []
        self._word_shown = []
        for i in self._word_hide:
            if i == " ":
                self.word_hide.append("\n")
            elif i == "-":
                self.word_hide.append("-")
            else:
                self.word_hide.append("_")
        for j in self.word_shown:
            if j == " ":
                self._word_shown.append("\n")
            else:
                self._word_shown.append(j)

    # def generate_sound(self):
    #     pass - доделать