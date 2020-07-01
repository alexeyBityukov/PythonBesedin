from random import randint

arrayLength = 20
numberOfEvenNumbers = 0
numberOfOddNumbers = 0

array = [randint(20,100) for x in range(arrayLength)]

for i in range(arrayLength):
    if array[i] % 2 == 0:
        numberOfEvenNumbers += 1
    else:
        numberOfOddNumbers += 1

print("Массив =", array,
      "\nКол-во четных чисел в массиве =", numberOfEvenNumbers,
      "\nКол-во нечетных чисел в массиве =", numberOfOddNumbers)
        
        
