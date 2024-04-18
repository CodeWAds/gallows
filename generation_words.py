from PyQt6.QtMultimedia import *
import random


class GenerationWords():

    # Слово, показываемое игроку
    def generate_open_word(self):

        self.random_index = random.randint(0, len(self.data[self.category_words])-1)

        if self.lang_index == 0:
            self.word_shown = self.data[self.category_words][self.random_index][0]

        else:
            self.word_shown = self.data[self.category_words][self.random_index][1]
        


    # Слово, которое игрок должен отгадать
    def generate_hidden_word(self):
        if self.lang_index == 0:
            self._word_hide = self.data[self.category_words][self.random_index][1]
        else:
            self._word_hide = self.data[self.category_words][self.random_index][0]
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
