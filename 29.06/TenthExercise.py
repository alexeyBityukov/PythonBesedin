import random

arrayLength = 10
array = []
isExistEvenPositiveElement = False

for i in range(0, arrayLength):
    array.append(random.randint(0, 10))


print('Массив значений = ', array)
array.sort()
print('Отсортированный массив значений = ', array)
alist = list(set(array))
alist.sort()
print('Уникальные элементы массива = ', alist)
