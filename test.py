from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap

class ImageManipulationApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.image_path = "src/img/stages_gallows/stage_0.png"  # Замените путем к вашему изображению

        self.pixmap = QPixmap(self.image_path)
        self.label = QLabel()
        self.label.setPixmap(self.pixmap)

        self.btn_zoom_in = QPushButton("Увеличить")
        self.btn_zoom_in.clicked.connect(self.zoom_in)

        self.btn_zoom_out = QPushButton("Уменьшить")
        self.btn_zoom_out.clicked.connect(self.zoom_out)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn_zoom_in)
        layout.addWidget(self.btn_zoom_out)

        self.setLayout(layout)

        self.setWindowTitle("Увеличение и уменьшение изображения")
        self.setGeometry(100, 100, 800, 600)

    def zoom_in(self):
        width = int(self.pixmap.width() * 1.2)
        height = int(self.pixmap.height() * 1.2)
        self.pixmap = self.pixmap.scaled(width, height)
        self.label.setPixmap(self.pixmap)

    def zoom_out(self):
        width = int(self.pixmap.width() / 1.2)
        height = int(self.pixmap.height() / 1.2)
        self.pixmap = self.pixmap.scaled(width, height)
        self.label.setPixmap(self.pixmap)

if __name__ == '__main__':
    app = QApplication([])
    main_app = ImageManipulationApp()
    main_app.show()
    app.exec()
