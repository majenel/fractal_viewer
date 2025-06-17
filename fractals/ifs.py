import random
from PySide6.QtCore import QPointF, QRectF

def draw_barnsley(painter, width, height, iterations=10000):
    # Масштаб и смещение для отображения
    scale = height / 12
    offset_x = width / 2
    offset_y = height

    x, y = 0, 0

    for _ in range(iterations):
        r = random.random()
        if r < 0.01:
            x1 = 0
            y1 = 0.16 * y
        elif r < 0.86:
            x1 = 0.85 * x + 0.04 * y
            y1 = -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            x1 = 0.2 * x - 0.26 * y
            y1 = 0.23 * x + 0.22 * y + 1.6
        else:
            x1 = -0.15 * x + 0.28 * y
            y1 = 0.26 * x + 0.24 * y + 0.44
        x, y = x1, y1

        px = int(offset_x + x * scale)
        py = int(offset_y - y * scale)

        painter.drawPoint(px, py)