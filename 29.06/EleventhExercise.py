import random

arrayLength = 10
array = []
numberIndexes = []
isExistNumber = False
number = int(input('введите искомое число: '))

for i in range(0, arrayLength):
    array.append(random.randint(0, 10))
    if(number == array[i]):
        isExistNumber = True
        numberIndexes.append(i)

print('Массив значений = ', array)
if(isExistNumber):
    print('Индексы значений введенного числа = ', numberIndexes)
else:
    print('Введенное число не существует в массиве')
array.sort(reverse=True)
print('Отсортированный массив значений = ', array)
        
