from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 400, 200)

        self.button = QPushButton('Нажми меня', self)
        self.label = QLabel('Пример текста', self)

        self.adjust_widget_sizes()  # Изначальная установка размеров виджетов

        self.show()

    def adjust_widget_sizes(self):
        button_width = self.width() // 4
        button_height = self.height() // 8

        label_width = self.width() // 2
        label_height = self.height() // 8

        self.button.setGeometry(10, 10, button_width, button_height)
        self.label.setGeometry(10, 50, label_width, label_height)

    def resizeEvent(self, event):
        self.adjust_widget_sizes()
        super().resizeEvent(event)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWidget()
    app.exec()
