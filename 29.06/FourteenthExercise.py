Fin = open ( "input.txt")
lineNumbers = 0;
sum = 0

while True:
    s = Fin.readline()
    if not s: break
    sum += int(s)
    lineNumbers+=1
Fin.close()

Fout = open ( "output.txt", "w")
Fout.write ( str(sum/lineNumbers) )
Fout.close()
