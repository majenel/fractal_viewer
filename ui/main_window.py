from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QListWidget, QVBoxLayout, QPushButton
import time


from canvas.canvas_widget import FractalCanvas
from fractals.koch import draw_koch, draw_snowflake
from fractals.dragon import draw as draw_dragon
from fractals.ifs import draw_barnsley


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Фракталы: Учебник")
        self.setMinimumSize(800, 600)

        # Главный виджет и компоновка
        central = QWidget()
        self.setCentralWidget(central)
        layout = QHBoxLayout(central)

        # Список фракталов слева
        self.list = QListWidget()
        self.list.addItems([
            "Кривая Коха",#
            "Снежинка Коха",#
            "Дракон Хартера-Хейтуэя",#
            "Кривая Гильберта",#
            "Множество Мандельброта",
            "IFS: Папоротник Барнсли",#
        ])
        self.list.currentTextChanged.connect(self.on_fractal_selected)
        layout.addWidget(self.list, 1)

        # Канва и кнопки справа
        right = QVBoxLayout()
        self.canvas = FractalCanvas()
        right.addWidget(self.canvas, stretch=1)

        self.morph_btn = QPushButton("Морфинг")
        self.morph_btn.clicked.connect(self.start_morphing)
        right.addWidget(self.morph_btn)

        layout.addLayout(right, 4)

    def on_fractal_selected(self, name):
        if name == "Кривая Коха":
            self.canvas.set_fractal(draw_koch, x2=100, y2=300, x1=700, y1=300, depth=0)
        elif name == "Снежинка Коха":
            self.canvas.set_fractal(draw_snowflake, x=100, y=300, size=200, depth=0)
        elif name == "Дракон Хартера-Хейтуэя":
            self.canvas.set_fractal(draw_dragon, x=100, y=300, length=200, angle=0, axiom="FX", ruleX="X+YF+", ruleY="-FX-Y", depth=0)
        elif name == "Кривая Гильберта":
            self.canvas.set_fractal(draw_dragon, x=100, y=300, length=200, angle=60, axiom="X", ruleX="-YF+XFX+FY-", ruleY="+XF-YFY-FX+", depth=0)
        elif name == "IFS: Папоротник Барнсли":
            self.canvas.set_fractal(draw_barnsley, width=self.canvas.width(), height=self.canvas.height(), iterations=0)
        elif name == "Множество Мандельброта":
            # Заглушка, пока не реализовано
            self.canvas.set_fractal(None)

    def start_morphing(self):
        print("Морфинг запускается...")
        # Пока просто заглушка