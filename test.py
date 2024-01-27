from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QIcon, QPixmap

class CustomDialog(QDialog):
    def __init__(self, title, text, image_path, parent=None):
        super().__init__(parent)

        self.setWindowTitle(title)

        layout = QVBoxLayout()

        label_text = QLabel(text)
        layout.addWidget(label_text)
        
        pixmap = QPixmap(image_path)
        label_image = QLabel()
        label_image.setPixmap(pixmap)
        layout.addWidget(label_image)

        button_ok = QPushButton('OK')
        button_ok.clicked.connect(self.accept)
        layout.addWidget(button_ok)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication([])

    dialog = CustomDialog("Победа!", "Поздравляем! Вы выиграли!", "path/to/image.png")
    dialog.exec()

    app.exec()