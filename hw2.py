# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint

n = int(input('Введите длину списка: '))
list = [0]*n
i = 0

while i < n:
    list[i] = randint(-42, 42)
    i += 1
print(list)

couple = 0
half = round(len(list)/2)

if len(list) % 2 == 0:
    j = half
else:
    j = half+1

for i in range(0, j):
    end = i+1
    couple = list[i] * list[-end]
    print(couple)
