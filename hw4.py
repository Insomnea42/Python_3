# Напишите программу, которая будет преобразовывать десятичное число в двоичное


def dd(n, list=[]):
    if n != 1:
        ost = round(n % 2)
        list.append(ost)
        dd(round(n/2), list)
    else:
        list.append(n)

n = int(input('Введите десятичное число: '))
list = []
new_list = []
dd(n, list)

for i in range(1, len(list)+1):
    new_list.append(list[-i])

print(new_list)
