istr = input('Введите строку для преобразования: ')
nstr = ''
for i in range(0, len(istr)):
    if(istr[i] == 'а'): nstr += 'б'
    elif(istr[i] == 'a'): nstr += 'b'
    elif(istr[i] == 'б'): nstr += 'а'
    elif(istr[i] == 'b'): nstr += 'a'
    elif(istr[i] == 'А'): nstr += 'Б'
    elif(istr[i] == 'A'): nstr += 'B'
    elif(istr[i] == 'Б'): nstr += 'А'
    elif(istr[i] == 'B'): nstr += 'A'
    else: nstr += istr[i]
print('Полученная строка: ', nstr)
