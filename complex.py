__author__ = 'ipetrash'

if __name__ == '__main__':
    # TODO: доделать
    # Комплексные числа (complex)
    # В Python встроены также и комплексные числа:

    x = complex(1, 2)
    print(x)

    y = complex(3, 4)
    print(y)

    z = x + y
    print(x)
    print(z)

    z = x * y
    print(z)

    z = x / y
    print(z)
    print(x.conjugate())  # Сопряжённое число
    print(x.imag)  # Мнимая часть
    print(x.real)  # Действительная часть
    # print ( x > y ) # Комплексные числа нельзя сравнить
    print(x == y)  # Но можно проверить на равенство
    # abs ( 3 + 4 j ) # Модуль комплексного числа
    # pow ( 3 + 4 j , 2 ) # Возведение в степень

    # Также для работы с комплексными числами используется также модуль cmath .