firtElement = int(input('First element: '))
sizeOfElement = int(input('Size of elements: '))
differenceBetweenNumbers = int(input('Difference between numbers: '))

array = []
array.append(firtElement)

for i in range(1, sizeOfElement):
    array.append(array[i-1] + differenceBetweenNumbers);
    
print('Arithmetic progression: ', array)
