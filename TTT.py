def print_field(f):
    """
    Функция печатает поле с координатами
    :param f: список списков (с координатами и содержимым поля)
    :return: None
    """
    for i in range(len(f)):
        print(*f[i])
    print('')


def user_input(f, c):
    """
    Функция проводит валидацию пользовательского ввода координат
    :param c: int - счетчик шагов
    :param f: список списков (с координатами и содержимым поля)
    :return: две координаты x, y
    """
    if c % 2 == 0:
        user = 'X'
    else:
        user = 'O'
    while True:
        coordinate = input(f'Ходит {user}. \nВведите координаты через пробел в формате "0 1": \n').split()
        if len(coordinate) != 2:
            print('Введите две координаты!')
            continue
        if not all([coordinate[0].isdigit(), coordinate[1].isdigit()]):
            print('Координаты должны быть числами!')
            continue
        x, y = map(int, coordinate)
        if not all([x >= 0, x < 3, y >= 0, y < 3]):
            print('Введите координаты в диапазоне [0; 2]')
            continue
        if f[x + 1][y + 1] != '-':
            print('Клетка занята')
            continue
        break
    return x, y, user


def win_check(f, user):
    """
    Функция проверки выигрышной ситуации
    :param f: список списков (с координатами и содержимым поля)
    :param user: строка с указанием, кто ходит "Х" или "О"
    :return: True - есть победитель, False - нет победителя
    """
    win_coords = (((0, 0), (0, 1), (0, 2)),  # Все горизонтали
                  ((1, 0), (1, 1), (1, 2)),  # Все горизонтали
                  ((2, 0), (2, 1), (2, 2)),  # Все горизонтали
                  ((0, 0), (1, 0), (2, 0)),  # Все вертикали
                  ((0, 1), (1, 1), (2, 1)),  # Все вертикали
                  ((0, 2), (1, 2), (2, 2)),  # Все вертикали
                  ((0, 0), (1, 1), (2, 2)),  # Диагональ (0;0) (2;2)
                  ((0, 2), (1, 1), (2, 0)),)  # Диагональ (0;2) (2;0)
    for coords in win_coords:
        symbols = []
        for coord in coords:
            symbols.append(f[coord[0] + 1][coord[1] + 1])
        if symbols == [user, user, user]:
            return True
    return False


# Пустое поле
field = [[' ', '0', '1', '2'],
         ['0', '-', '-', '-'],
         ['1', '-', '-', '-'],
         ['2', '-', '-', '-']]

count = 0
while True:
    print_field(field)
    if count < 9:
        x, y, user = user_input(field, count)
        field[x + 1][y + 1] = user
    if count == 9:
        print('Ничья!')
        break
    if win_check(field, user):
        print(f"Выиграл {user}")
        break
    count += 1
