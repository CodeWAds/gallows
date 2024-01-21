import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class VirtualKeyboard(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Создаем поле ввода
        self.text_edit = QLineEdit(self)
        layout.addWidget(self.text_edit)

        # Создаем кнопки английской клавиатуры
        english_keys = [
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
        ]

        english_layout = QVBoxLayout()
        for row in english_keys:
            key_row = QHBoxLayout()
            for key in row:
                button = QPushButton(key, self)
                button.clicked.connect(self.on_key_clicked)
                key_row.addWidget(button)
            english_layout.addLayout(key_row)

        # Создаем кнопки русской клавиатуры
        russian_keys = [
            ['Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З'],
            ['Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д'],
            ['Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю']
        ]

        russian_layout = QVBoxLayout()
        for row in russian_keys:
            key_row = QHBoxLayout()
            for key in row:
                button = QPushButton(key, self)
                button.clicked.connect(self.on_key_clicked)
                key_row.addWidget(button)
            russian_layout.addLayout(key_row)

        # Добавляем оба комплекта кнопок в основной layout
        layout.addLayout(english_layout)
        layout.addLayout(russian_layout)

        self.setLayout(layout)

        self.setWindowTitle('Virtual Keyboard')
        self.show()

    def on_key_clicked(self):
        button = self.sender()
        current_text = self.text_edit.text()
        clicked_text = button.text()
        self.text_edit.setText(current_text + clicked_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    keyboard = VirtualKeyboard()
    sys.exit(app.exec())
