from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QGraphicsDropShadowEffect
from PyQt6.QtGui import QPixmap
import sys

class RoundedImageApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        
        # Создаем графическое окно
        self.view = QGraphicsView()
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)

        # Загружаем изображение
        pixmap = QPixmap("src/stages_with_bg/stage_4.png")

        # Создаем элемент с изображением
        pixmap_item = QGraphicsPixmapItem(pixmap)
        
        # Создаем эффект для закругленных краев
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(10)  # Радиус размытия
        shadow_effect.setColor("#000000")  # Цвет тени
        shadow_effect.setOffset(0, 0)  # Смещение тени

        # Применяем эффект к элементу с изображением
        pixmap_item.setGraphicsEffect(shadow_effect)

        # Добавляем элемент с изображением на сцену
        self.scene.addItem(pixmap_item)

        # Устанавливаем закругленные края для элемента
        pixmap_item.setShapeMode(QGraphicsPixmapItem.ShapeMode.BoundingRect)

        # Отображаем графическое окно
        self.view.show()

if __name__ == "__main__":
    app = RoundedImageApp(sys.argv)
    sys.exit(app.exec())