parameters = list(map(str, input('Введите оператор и два положительных целых числа через пробел:>').split(sep=' ')))
# assert parameters[0] in ['+', '-', '*', '/'], print('Введённый оператор не поддерживается, используйте + - * /')
try:
    parameters[1], parameters[2] = int(parameters[1]), int(parameters[2])
except:
    print("TypeError")

print(parameters)
