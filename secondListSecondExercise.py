arrayLength = int(input("Введите длинну массива: "))
array = []
maxValue = None
numberOfMaximumValues = 0

for i in range(arrayLength):
    inputElem = int(input("%d-й элемент массива: " % (i)))
    array.append(inputElem)
    if maxValue is None :
        maxValue = inputElem
    elif maxValue < inputElem :
        numberOfMaximumValues = 1
        maxValue = inputElem
    elif maxValue == inputElem : 
        numberOfMaximumValues += 1

print("Количсево максимальных элементов:", numberOfMaximumValues)

        
        
