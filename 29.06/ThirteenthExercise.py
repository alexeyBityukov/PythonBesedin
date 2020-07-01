import random

arrayLength = 10
arrayHeight = 10
matrix = []

for i in range(0, arrayLength):
    line = []
    for j in range(0, arrayHeight):
        line.append(random.randint(0, 100))
        if(i == 0 and j == 0):
            minElem = line[j]
            indexJMin = j
            indexIMin = i
            maxElem = line[j]
            indexJMax = j
            indexIMax = i
        if(minElem > line[j]):
            minElem = line[j]
            indexJMin = j
            indexIMin = i
        if(maxElem < line[j]):
            maxElem = line[j]
            indexJMax = j
            indexIMax = i
    matrix.append(line)

print('Исходная матрица = ', matrix)
print('Минимальный элемент = ', minElem)
print('Индексы минимального элемента = [', indexIMin, ',', indexJMin, ']')
print('Максимальный элемент = ', maxElem)
print('Индексы максимального элемента = [', indexIMax, ',', indexJMax, ']')
