from random import randint

arrayLength = 20
numberOfNumbersSought = 0

array = [randint(1000,2000) for x in range(arrayLength)]

for i in range(arrayLength):
    secondDigitFromEnd = array[i] % 100 // 10
    if secondDigitFromEnd % 2 == 0 :
        numberOfNumbersSought += 1

print("Массив =", array,
      "\nКол-во элементов массива у которых вторая с конца цифра четная =",
      numberOfNumbersSought)
