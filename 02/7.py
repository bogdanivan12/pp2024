n = int(input("n = "))
c = int(input("c = "))

cifre = 0
nr = n
while nr != 0:
    cifre = cifre + 1
    nr = nr // 10

rezultat = (c * 10 ** cifre + n) * 10 + c
print(rezultat)
