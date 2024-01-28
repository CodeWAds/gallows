from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Нажми меня", self)
        self.button.setGeometry(50, 50, 100, 30)
        self.button.clicked.connect(self.mouseDoubleClickEvent)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            print("Двойной щелчок на кнопке")

    def on_button_click(self):
        print("Клик на кнопке")

if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.setGeometry(100, 100, 300, 200)
    widget.show()
    app.exec()
