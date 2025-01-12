f = open("numere.txt", "r")
v = [int(x) for x in f.read().split()]
f.close()


def este_prim(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def cauta_prim(v, st, dr):
    if st == dr:
        return este_prim(v[st])
    mij = (dr + st) // 2
    return cauta_prim(v, st, mij) or cauta_prim(v, mij + 1, dr)


print(cauta_prim(v, 0, len(v) - 1))
