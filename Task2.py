result = ''
parameters = list(
    map(str, input('Введите оператор и два положительных целых числа через пробел (например, + 2 2):>').split(sep=' ')))
try:
    assert parameters[0] in ['+', '-', '*', '/']
    parameters[1] = int(parameters[1])
    parameters[2] = int(parameters[2])
    if parameters[0] == '+':
        result = parameters[1] + parameters[2]
    elif parameters[0] == '-':
        result = parameters[1] - parameters[2]
    elif parameters[0] == '*':
        result = parameters[1] * parameters[2]
    elif parameters[0] == '/':
        result = parameters[1] / parameters[2]
except AssertionError:
    print('Введённый оператор не поддерживается, используйте "+" или "-" или "*" или "/"')
except ZeroDivisionError:
    print('Попытка разделить на ноль')
except IndexError:
    print('Введено недостаточное количество параметров операции для расчёта')
except ValueError:
    print(f'Один из операндов не является числом')
else:
    print(f'{parameters[1]} {parameters[0]} {parameters[2]} = {result}')
finally:
    if result == '':
        print('Вычисление выполнить не удалось. Вы ввели некорректные данные.')
