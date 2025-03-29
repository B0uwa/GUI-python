from PyQt5 import QtWidgets, uic
import math
import numpy as np
import matplotlib.pyplot as plt
import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

app_ball = QtWidgets.QApplication([])
ui = uic.loadUi("waves.ui")
ui.setWindowTitle("расчет траектории полета")

def calc():
    A = ui.doubleSpinBox_1.value()
    N = ui.doubleSpinBox_2.value()
    alpha_Gr = ui.doubleSpinBox_3.value()
    alpha = math.radians(alpha_Gr)

    T = (1/N) * 4
    T = int(round(T, 2) * 100)
    t_i = []
    for i in range(T):  # создаем массив с разбитым времени
        t_i.append(i/100)
    x = []
    for t_part in t_i:
        x.append(A * math.sin(2 * math.pi * N * t_part + alpha))


    global window_s #объявляем глобальной чтобы не удалялся после выходы из функции
    window_s = QWidget()
    window_s.setWindowTitle('Гарфик x(t)')
    window_s.resize(800, 600)

    fig = Figure(figsize=(8, 6))
    gr = fig.add_subplot(111) # создает оси (графическую область) на фигуре fig, 111 параметр, определяющий расположение графика (сетка 1 на 1)


    gr.plot(t_i, x, 'b-', linewidth=2)
    gr.set_title('Траектория полета тела')
    gr.set_xlabel(' время (с)')
    gr.set_ylabel('смещение (м)')
    gr.grid(True)

    gr.set_aspect('equal', adjustable='box') #чтобы оси были эквиваентны

    canvas = FigureCanvas(fig) #Создаем виджет FigureCanvas, который будет отображать наш график matplotlib
    layout = QVBoxLayout() #Создаем вертикальный компоновщик
    layout.addWidget(canvas) #Теперь график будет основным элементом окна
    window_s.setLayout(layout)  #Устанавливаем созданный слой как основной для окна window_s
    window_s.show() #Делаем окно window_s видимым на экране

ui.pushButton_1.clicked.connect(calc)
ui.show()
app_ball.exec()






