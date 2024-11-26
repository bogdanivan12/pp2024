n, m = input().split()
n = int(n)
m = int(m)
mat = []
for i in range(n):
    mat.append([int(x) for x in input().split()])

suma = sum([sum([x for x in linie if x % 2 == 0]) for linie in mat])
print(suma)
