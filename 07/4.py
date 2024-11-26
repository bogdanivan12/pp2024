m, n = [int(x) for x in input().split()]
mat = []
for i in range(m):
    mat.append([int(x) for x in input().split()])

sume = [sum(linie) for linie in mat]
print(sume)
print(sume.count(max(sume)))
