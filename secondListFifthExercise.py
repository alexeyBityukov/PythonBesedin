from random import randint

arrayLength = 20

array = [randint(0,4) for x in range(arrayLength)]

inputNumber = int(input("Введите X: "))
print("Массив:", array, "\nНомера элементов равных X: ", end = '')

for i in range(arrayLength):
    if inputNumber == array[i] :
        print(i, end = ' ')
