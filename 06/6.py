ls = [float(x) for x in input().split()]
for i in range(len(ls) - 1, -1, -1):
    if ls[i] < 0:
        ls.insert(i + 1,0)
print(ls)
