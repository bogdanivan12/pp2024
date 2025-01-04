def suma(v):
    if len(v) == 1:
        return v[0]
    mijloc = len(v) // 2
    return suma(v[:mijloc]) + suma(v[mijloc:])


lista = [int(x) for x in input().split()]
print(suma(lista))
