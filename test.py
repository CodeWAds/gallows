from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6 import QtGui, QtCore
import sys

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.sound_word = QPushButton(self)
        self.sound_word.setGeometry(670, 20, 48, 48)
        self.sound_word.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        pixmap = QPixmap("src/img/sound_word.png")
        icon = QIcon(pixmap)
        self.sound_word.setIcon(icon)
        self.sound_word.setIconSize(pixmap.size())

        # Установка кнопки в режиме без обводки
        self.sound_word.setFlat(True)

        self.sound_word.clicked.connect(self.sound_words)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('No Border Button Example')

    def sound_words(self):
        print('Sound button clicked!')

def main():
    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
