def suma(v):
    if len(v) == 1:
        return v[0]
    return v[0] + suma(v[1:])


lista = [int(x) for x in input().split()]
print(suma(lista))
