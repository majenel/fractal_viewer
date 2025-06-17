from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen
from PySide6.QtCore import Qt, QPointF


class FractalCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.fractal_func = None
        self.fractal_args = {}
        self.zoom = 1.0
        self.offset = QPointF(0, 0)
        self.last_mouse_pos = None

    def set_fractal(self, func, **kwargs):
        self.fractal_func = func
        self.fractal_args = kwargs
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.white)
        if self.fractal_func:
            pen = QPen(Qt.black)
            painter.setPen(pen)
            painter.translate(self.offset)
            painter.scale(self.zoom, self.zoom)
            self.fractal_func(painter, **self.fractal_args)

    def wheelEvent(self, event):
        delta = event.angleDelta().y()
        factor = 1.2 if delta > 0 else 1 / 1.2
        mouse_pos = event.position()
        before = (mouse_pos - self.offset) / self.zoom

        self.zoom *= factor
        after = (mouse_pos - self.offset) / self.zoom
        self.offset += (after - before) * self.zoom
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_mouse_pos = event.position()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self.last_mouse_pos:
            delta = event.position() - self.last_mouse_pos
            self.offset += delta
            self.last_mouse_pos = event.position()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_mouse_pos = None