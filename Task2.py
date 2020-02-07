result = 0
parameters = list(map(str, input('Введите оператор и два положительных целых числа через пробел (например, + 2 2):>').split(sep=' ')))
try:
    assert parameters[0] in ['+', '-', '*', '/'], print('Введённый оператор не поддерживается, используйте + - * /')
except:
    pass
parameters[1], parameters[2] = int(parameters[1]), int(parameters[2])
if parameters[0] == '+':
    result = parameters[1] + parameters[2]
elif parameters[0] == '-':
    result = parameters[1] - parameters[2]
elif parameters[0] == '*':
    result = parameters[1] * parameters[2]
elif parameters[0] == '/':
    result = parameters[1] / parameters[2]
# assert parameters[0] in ['+', '-', '*', '/'], print('Введённый оператор не поддерживается, используйте + - * /')
# try:
#     parameters[1] = int(parameters[1])
# except ValueError:
#     print("Первый операнд не является числом")
# try:
#     parameters[2] = int(parameters[2])
# except ValueError:
#     print("Второй операнд не является числом")

print(result)
