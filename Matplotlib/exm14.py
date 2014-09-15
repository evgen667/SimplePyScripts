__author__ = 'ipetrash'


import math

# !!! Импортируем один из пакетов Matplotlib
import pylab

# !!! Импортируем пакет со вспомогательными функциями
from matplotlib import mlab

# Будем рисовать график этой функции
def func(x):
    """
    sinc (x)
    """
    if x == 0:
        return 1.0
    return math.sin(x) / x


if __name__ == '__main__':
    # Интервал изменения переменной по оси X
    xmin = -20.0
    xmax = 20.0

    # Шаг между точками
    dx = 0.2

    # !!! Создадим список координат по оси X на отрезке [-xmin; xmax], включая концы
    xlist = mlab.frange (xmin, xmax, dx)

    # Вычислим значение функции в заданных точках
    ylist = [func (x) for x in xlist]

    # # !!! Нарисуем одномерный график с использованием стиля
    # pylab.plot(xlist, ylist, "x")
    #
    # Второй способ задания стиля
    # Другой способ более гибкий, в том числе в плане задания цветов. Он состоит в том,
    # чтобы в явном виде задавать различные параметры линии. В этом случае один параметр,
    # который отвечал за стиль в прошлых примерах, разобьем на несколько параметров:
    # color или c - задает цвет.
    # marker - задает вид маркера.
    # linestyle - стиль линии.
    #
    # Кроме того, можно использовать дополнительные параметры. Например:
    # markerfacecolor - цвет маркеров.
    # markersize - размер маркера.
    # linewidth или lw - толщина линии.
    # Есть еще и другие параметры, но о них мы пока говорить не будем.
    # Если в первом способе мы были ограничены восемью цветами, то теперь цвета
    # настраиваются более гибко. О том, как можно задавать цвета я уже писал в статье
    # про рисование трехмерных графиков. Здесь цвета задаются точно так же.
    # Пример
    # pylab.plot (xlist, ylist, "-*k")
    # можно изменить следующим образом:
    # pylab.plot (xlist, ylist, linestyle = "-", marker = "*", color = "k")
    # Результат будет выглядеть точно также. А, например, следующий код

    pylab.plot(xlist, ylist, linestyle="-", marker="o", color="k",
               markerfacecolor="#ff22aa")

    # !!! Покажем окно с нарисованным графиком
    pylab.show()