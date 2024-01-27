from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создайте кнопку
        button = QPushButton('Показать всплывающее окно', self)
        button.clicked.connect(self.show_popup)

        # Установите кнопку в центр главного окна
        self.setCentralWidget(button)

    def show_popup(self):
        # Создайте всплывающее окно QMessageBox
        popup = QMessageBox()

        # Установите заголовок, текст и тип всплывающего окна
        popup.setWindowTitle('Всплывающее окно')
        popup.setText('Это всплывающее окно с сообщением.')
        popup.setIcon(QMessageBox.Icon.Information)

        # Добавьте кнопки (по желанию)
        popup.addButton('ОК', QMessageBox.ButtonRole.AcceptRole)
        

        # Показать всплывающее окно и дождаться ответа
        result = popup.exec()

        # Обработать результат
        if result == QMessageBox.StandardButton:
            print('Нажата кнопка "ОК"')
        else:
            print('Нажата кнопка "Отмена"')

if __name__ == '__main__':
    app = QApplication([])

    # Создайте главное окно
    main_window = MainWindow()
    main_window.show()

    app.exec()
