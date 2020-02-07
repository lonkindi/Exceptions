result = 0
parameters = list(
    map(str, input('Введите оператор и два положительных целых числа через пробел (например, + 2 2):>').split(sep=' ')))
parameters[1], parameters[2] = int(parameters[1]), int(parameters[2])
if parameters[0] == '+':
    result = parameters[1] + parameters[2]
elif parameters[0] == '-':
    result = parameters[1] - parameters[2]
elif parameters[0] == '*':
    result = parameters[1] * parameters[2]
elif parameters[0] == '/':
    result = parameters[1] / parameters[2]
print(result)
