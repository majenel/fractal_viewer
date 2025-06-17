from PySide6.QtCore import QPointF
import math


def draw_koch(painter, x1, y1, x2, y2, depth):
    if depth == 0:
        painter.drawLine(QPointF(x1, y1), QPointF(x2, y2))
        return

    dx = (x2 - x1) / 3
    dy = (y2 - y1) / 3
    xA = x1 + dx
    yA = y1 + dy
    xB = x1 + 2 * dx
    yB = y1 + 2 * dy

    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    hx = mx + math.sqrt(3) * (y1 - y2) / 6
    hy = my + math.sqrt(3) * (x2 - x1) / 6

    draw_koch(painter, x1, y1, xA, yA, depth - 1)
    draw_koch(painter, xA, yA, hx, hy, depth - 1)
    draw_koch(painter, hx, hy, xB, yB, depth - 1)
    draw_koch(painter, xB, yB, x2, y2, depth - 1)


def draw_snowflake(painter, x, y, size, depth):
    for i in range(3):
        angle1 = math.radians(120 * i)
        angle2 = math.radians(120 * (i + 1))
        x1 = x + size * math.cos(angle1)
        y1 = y + size * math.sin(angle1)
        x2 = x + size * math.cos(angle2)
        y2 = y + size * math.sin(angle2)
        draw_koch(painter, x2, y2, x1, y1, depth)
