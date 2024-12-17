def citire_lista():
    return [int(x) for x in input().split()]


def nr_div_proprii(n):
    nr_div = 0
    for nr in range(2, n):
        if n % nr == 0:
            nr_div += 1
    return nr_div
    # SAU
    # return len([nr for nr in range(2, n) if n % nr == 0])


lista = citire_lista()
k = int(input())
sol = [x for x in lista if nr_div_proprii(x) < k]
sol = sorted(list(set(sol)))
for x in sol:
    print(x, end=" ")
