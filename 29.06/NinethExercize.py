import random

arrayLength = 10
array = []
isExistEvenPositiveElement = False

for i in range(0, arrayLength):
    array.append(random.randint(-1000, 1000))
    if(array[i]%2 == 0 and array[i] > 0):
        if(not isExistEvenPositiveElement):
            minEvenPositiveElement = array[i]
            maxEvenPositiveElement = array[i]
        isExistEvenPositiveElement = True
        if(minEvenPositiveElement > array[i]):
            minEvenPositiveElement = array[i]
        if(maxEvenPositiveElement < array[i]):
            maxEvenPositiveElement = array[i]

if(not isExistEvenPositiveElement):
    print('Нет чётных положительных элементов')
else:
    print('Максимальный чётный положительный элемент = ', maxEvenPositiveElement)
    print('Минимальный чётный положительный элемент = ', minEvenPositiveElement)
print('Массив значений = ', array)
