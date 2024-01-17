from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore, QtGui, QtWidgets
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi()

    def change_lang(self):
        self.lang_button.setText("")

    def setupUi(self):
        # Установка окна
        self.setObjectName("MainWindow")
        self.setFixedSize(720, 480)
        self.setStyleSheet("background-color: rgb(140, 83, 255);\n"
                           "font: 16pt \"Fixedsys\"")
        self.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)

        # Устанавливаем изображения
        self.image_paths = ['src/RF.png', 'src/UK.png']
        self.current_image_index = 0
        self.loadImage()
        
        # Название игры в окне
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")

        self.name_game = QtWidgets.QLabel(parent=self.centralwidget)
        self.name_game.setGeometry(QtCore.QRect(310, 100, 100, 20))
        self.name_game.setStyleSheet("font-size: 20pt;\n"
                                     "")
        self.name_game.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_game.setObjectName("name_game")
        
        self.name_game.setText("Виселица")

        self.lang_button = QPushButton("Сменить\n"
                                       "язык", self)

        self.lang_button.setGeometry(QtCore.QRect(10, 40, 70, 30))
        self.lang_button.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.lang_button.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        self.lang_button.setAutoFillBackground(False)
        self.lang_button.setStyleSheet("border: 1px solid #dfe6e9;\n"
                                       "background-color: #a29bfe;\n"
                                       "border-radius: 5px;\n"
                                       "font: 12pt \"Fixedsys\""
                                       "")
        self.lang_button.setObjectName("lang_button")

        self.lang_button.clicked.connect(self.change_lang)

        self.pushButton = QPushButton("СТАРТ", self)

        self.pushButton.setGeometry(QtCore.QRect(280, 260, 160, 40))
        self.pushButton.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("border: 1px solid #dfe6e9;\n"
                                      "background-color: #a29bfe;\n"
                                      "border-radius: 5px;\n"
                                      "padding: 50px;\n"
                                      "")
        self.pushButton.setObjectName("start_button")
        # self.pushButton.clicked.connect(self.change_l)

        self.setCentralWidget(self.centralwidget)

        self.setWindowTitle("Виселица")
        

# class ImageDisplay(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         # Создаем виджет QLabel
#         self.label = QLabel(self)

#         # Создаем кнопку для изменения изображения
#         self.button = QPushButton('Изменить изображение', self)
#         self.button.clicked.connect(self.toggleImage)

#         # Устанавливаем кнопку и QLabel в макет
#         layout = QVBoxLayout()
#         layout.addWidget(self.label)
#         layout.addWidget(self.button)

#         # Создаем основной виджет и устанавливаем в него главный макет
#         central_widget = QWidget()
#         central_widget.setLayout(layout)

#         # Устанавливаем центральный виджет в главное окно
#         self.setCentralWidget(central_widget)

#         # Устанавливаем изображения
#         self.image_paths = ['src/RF.png', 'src/UK.png']
#         self.current_image_index = 0
#         self.loadImage()

#         # Устанавливаем заголовок окна
#         self.setWindowTitle('Image Display')

#     def loadImage(self):
#         # Загружаем изображение в QPixmap
#         pixmap = QPixmap(self.image_paths[self.current_image_index])
#         self.label.setPixmap(pixmap)
#         self.resize(pixmap.width(), pixmap.height())

#     def toggleImage(self):
#         # Переключаем индекс изображения
#         self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
#         self.loadImage()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
