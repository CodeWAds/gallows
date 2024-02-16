from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QSize

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

    def resizeEvent(self, event):
        # Получаем текущий размер виджета
        current_size = event.size()
        print("Текущий размер:", current_size)

        # Получаем предыдущий размер виджета
        old_size = event.oldSize()
        print("Предыдущий размер:", old_size)

if __name__ == "__main__":
    app = QApplication([])
    widget = MyWidget()
    widget.resize(300, 200)
    widget.show()
    app.exec()
