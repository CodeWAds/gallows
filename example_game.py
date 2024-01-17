import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtGui import QFont

class HangmanGame(QWidget):
    def __init__(self):
        super().__init__()

        self.word_to_guess = "PYQT6"  # Слово для угадывания
        self.guess_word = ["_"] * len(self.word_to_guess)  # Слово, которое отображается пользователю

        self.attempts_left = 6  # Количество попыток

        self.init_ui()

    def init_ui(self):
        # Создаем виджеты
        self.word_label = QLabel(self)
        self.word_label.setFont(QFont("Arial", 16))
        self.update_word_label()

        self.attempts_label = QLabel(f"Attempts left: {self.attempts_left}", self)
        self.attempts_label.setFont(QFont("Arial", 12))

        self.guess_input = QLineEdit(self)

        self.guess_button = QPushButton("Guess", self)
        self.guess_button.clicked.connect(self.make_guess)

        # Размещаем виджеты в макете
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.word_label)
        v_layout.addWidget(self.attempts_label)
        v_layout.addWidget(self.guess_input)
        v_layout.addWidget(self.guess_button)

        # Устанавливаем основной макет
        self.setLayout(v_layout)

        # Устанавливаем параметры окна
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Hangman Game')
        self.show()

    def update_word_label(self):
        self.word_label.setText(" ".join(self.guess_word))

    def make_guess(self):
        guess = self.guess_input.text().upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in self.word_to_guess:
                for i, letter in enumerate(self.word_to_guess):
                    if letter == guess:
                        self.guess_word[i] = guess
                self.update_word_label()
            else:
                self.attempts_left -= 1
                self.attempts_label.setText(f"Attempts left: {self.attempts_left}")

            if "_" not in self.guess_word:
                self.word_label.setText("Congratulations! You guessed the word.")
                self.guess_input.setDisabled(True)
                self.guess_button.setDisabled(True)
            elif self.attempts_left == 0:
                self.word_label.setText(f"Sorry, you lost. The word was {self.word_to_guess}.")
                self.guess_input.setDisabled(True)
                self.guess_button.setDisabled(True)
        else:
            self.word_label.setText("Please enter a valid single letter.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = HangmanGame()
    sys.exit(app.exec())
