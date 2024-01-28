from PyQt6.QtWidgets import QApplication, QDoubleSpinBox, QVBoxLayout, QWidget

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        double_spin_box = QDoubleSpinBox(self)
        double_spin_box.setDecimals(2)  # Устанавливаем количество знаков после запятой
        double_spin_box.editingFinished.connect(self.double_clicked)  # Подключаем обработчик события editingFinished

        layout.addWidget(double_spin_box)
        self.setLayout(layout)

    def double_clicked(self):
        print("Двойное нажатие кнопки! Значение:", self.sender().value())

if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec()
