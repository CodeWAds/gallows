from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import QTimer

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.button = QPushButton('Кнопка', self)
        self.button.clicked.connect(self.onButtonClick)

        layout.addWidget(self.button)

        self.setLayout(layout)
        self.single_click_enabled = True  # Флаг разрешения одиночного клика

    def onButtonClick(self):
        if self.single_click_enabled:
            # Выполните ваш код для одиночного клика здесь
            print('Одиночный клик')
            
            # Запретите двойной клик на кнопке на некоторое время
            self.single_click_enabled = False
            
            # Установите таймер для восстановления возможности двойного клика через 1 секунду
            timer = QTimer(self)
            timer.timeout.connect(self.enableSingleClick)
            timer.start(2000)  # 1000 миллисекунд = 1 секунда

    def enableSingleClick(self):
        # Восстановите возможность одиночного клика после завершения таймера
        self.single_click_enabled = True


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
