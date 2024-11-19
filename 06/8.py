l = [int(x) for x in input().split()]
maxim = max(l)
minim = min(l)
diferenta = maxim - minim
print(l.count(diferenta))

# SAU
print(l.count(max(l) - min(l)))
