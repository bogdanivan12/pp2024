ls=[int(x) for x in input().split()]
k=int(input())
smin=sum(ls[:k])
poz=0
for i in range(len(ls) - k):
    suma = sum(ls[i:i + k])
    if suma < smin:
        smin = suma
        poz = i
ls[poz:poz + k] = []
print(ls)
