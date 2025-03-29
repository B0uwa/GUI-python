from PyQt5 import QtWidgets, uic
import math
import numpy as np
import matplotlib.pyplot as plt
import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

app_ball = QtWidgets.QApplication([])
ui = uic.loadUi("Temp for H.ui")
ui.setWindowTitle("вводные")

def calc():
    T0 = ui.doubleSpinBox_1.value()
    Tk = ui.doubleSpinBox_2.value()
    k = ui.doubleSpinBox_3.value()
    # теперь через условия подберем время моделирования
    if k == 0:  # если нет охлаждения
        t_max = 10  # берем 10 секунд
    else:
        t_max = 5 / k  # 5 периодов охлаждения по Ньютону

    step = t_max / 500  # шаг по времени
    T = []
    t_i = []
    for i in range(500):
        t_i.append(i*step)
        T.append(Tk + (T0 - Tk) * math.exp(-k * (i * step)))

    global window_s #объявляем глобальной чтобы не удалялся после выходы из функции
    window_s = QWidget()
    window_s.setWindowTitle('Гарфик x(t)')
    window_s.resize(800, 600)

    fig = Figure(figsize=(8, 6))
    gr = fig.add_subplot(111) # создает оси (графическую область) на фигуре fig, 111 параметр, определяющий расположение графика (сетка 1 на 1)


    gr.plot(t_i, T, 'b-', linewidth=2)
    gr.set_title('теплообмен')
    gr.set_xlabel(' время (с)')
    gr.set_ylabel('Y — температура тела (°C)')
    gr.grid(True)



    canvas = FigureCanvas(fig) #Создаем виджет FigureCanvas, который будет отображать наш график matplotlib
    layout = QVBoxLayout() #Создаем вертикальный компоновщик
    layout.addWidget(canvas) #Теперь график будет основным элементом окна
    window_s.setLayout(layout)  #Устанавливаем созданный слой как основной для окна window_s
    window_s.show() #Делаем окно window_s видимым на экране

ui.pushButton_1.clicked.connect(calc)
ui.show()
app_ball.exec()






