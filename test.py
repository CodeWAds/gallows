import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QUrl, QTimer

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.button = QPushButton('Нажми меня', self)
        self.button.clicked.connect(self.buttonClicked)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Пример с QTimer')
        self.show()

    def buttonClicked(self):
        self.button.setEnabled(False)

        # Создаем таймер на 2 секунды
        timer = QTimer(self)
        timer.singleShot(2000, self.enableButton)

    def enableButton(self):
        self.button.setEnabled(True)

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
