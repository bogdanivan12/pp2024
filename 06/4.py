ls = [int(x) for x in input().split()]
poz1 = ls.index(0)
poz2 = ls.index(0, poz1 + 1)
ls[poz1:poz2+1] = []  # ls = ls[:poz1] + ls[poz2+1:]
print(ls)
