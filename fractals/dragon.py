import math
from PySide6.QtCore import QPointF

def generate_l_system(axiom, rules, depth):
    result = axiom
    for _ in range(depth):
        result = ''.join(rules.get(c, c) for c in result)
    return result

def draw(painter, x, y, angle, axiom, ruleX, ruleY, depth, f="F", length=100):
    stack = []
    rules = {
        "X": ruleX,
        "Y": ruleY
    }
    commands = generate_l_system(axiom, rules, depth)

    # Масштабирование шага
    scaled_length = length / (2 ** (depth / 2))

    pos = QPointF(x, y)
    for cmd in commands:
        if cmd == f:
            rad = math.radians(angle)
            new_pos = QPointF(
                pos.x() + scaled_length * math.cos(rad),
                pos.y() + scaled_length * math.sin(rad)
            )
            painter.drawLine(pos, new_pos)
            pos = new_pos
        elif cmd == '+':
            angle += 90
        elif cmd == '-':
            angle -= 90
        elif cmd == '[':
            stack.append((pos, angle))
        elif cmd == ']':
            pos, angle = stack.pop()