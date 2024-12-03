file = open('matrice.in','r')
mat = [[int(x) for x in linie.split()] for linie in file.readlines()]
file.close()
k = int(input())

k_div_proprii = []
for linie in mat :
    for element in linie :
        nr_div = 0
        for i in range(2, element // 2 + 1):
            if element % i == 0:
                nr_div += 1
        if nr_div == k:
            k_div_proprii.append(element)
k_div_proprii.sort(reverse=True)
print(*k_div_proprii)

maxim = 0
for linie in mat:
    multime = set(linie)
    if len(multime) > maxim:
        maxim = len(multime)
for linie in mat:
    multime = set(linie)
    if len(multime) == maxim:
        print(linie)
