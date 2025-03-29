from PyQt5 import QtWidgets, uic
import math
import numpy as np
import matplotlib.pyplot as plt
import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

app_ball = QtWidgets.QApplication([])
ui = uic.loadUi("ball.ui")
ui.setWindowTitle("расчет траектории полета")

def calc():
    v = ui.spinBox_1.value()
    alpha_Gr = ui.spinBox_2.value()
    alpha = math.radians(alpha_Gr)
    g = 9.81
    t = 2 * v * math.sin(alpha) / g
    t = int(round(t, 2) * 100)
    t_i = []
    for i in range(t):  #создаем массив с разбитым временем
        t_i.append(i / 100)
    t_i.append(t_i[-1]+0.01)
    x = []
    y = []
    for t_part in t_i: #расчитываем координаты
        x.append(v * math.cos(alpha) * t_part)
        y.append(v * math.sin(alpha) * t_part - 0.5 * g * t_part ** 2)

    global window_s #объявляем глобальной чтобы не удалялся после выходы из функции
    window_s = QWidget()
    window_s.setWindowTitle('Траектория полета тела')
    window_s.resize(800, 600)

    fig = Figure(figsize=(8, 6))
    gr = fig.add_subplot(111) # создает оси (графическую область) на фигуре fig, 111 параметр, определяющий расположение графика (сетка 1 на 1)


    gr.plot(x, y, 'b-', linewidth=2)
    gr.set_title('Траектория полета тела')
    gr.set_xlabel('Расстояние (м)')
    gr.set_ylabel('Высота (м)')
    gr.grid(True)

    sr = y[len(y) // 2]

    gr.set_xlim(0, x[-1]+10)
    gr.set_ylim(0, sr+10)

    gr.set_aspect('equal', adjustable='box') #чтобы оси были эквиваентны

    canvas = FigureCanvas(fig) #Создаем виджет FigureCanvas, который будет отображать наш график matplotlib
    layout = QVBoxLayout() #Создаем вертикальный компоновщик
    layout.addWidget(canvas) #Теперь график будет основным элементом окна
    window_s.setLayout(layout)  #Устанавливаем созданный слой как основной для окна window_s
    window_s.show() #Делаем окно window_s видимым на экране

ui.pushButton_1.clicked.connect(calc)
ui.show()
app_ball.exec()






