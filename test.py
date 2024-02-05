from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Диалоговое окно")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        label = QLabel("Пример диалогового окна")
        layout.addWidget(label)

        closeButton = QPushButton("Закрыть")
        closeButton.clicked.connect(self.close)  # Подключение кнопки к закрытию диалога
        layout.addWidget(closeButton)

        self.setLayout(layout)

    def closeEvent(self, event):
        self.my_custom_function()
        event.accept()  # Закрыть диалог

    def my_custom_function(self):
        print("Функция при закрытии диалога")

if __name__ == "__main__":
    app = QApplication([])

    dialog = MyDialog()
    dialog.exec()

    app.exec()
