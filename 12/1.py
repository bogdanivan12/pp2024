f = open("date.in", "r")
v = [int(x) for x in f.read().split()]
f.close()


def cauta_varf(v, st, dr):
    if st == dr:
        return v[st]
    mij = (dr + st) // 2
    if v[mij] < v[mij + 1]:
        return cauta_varf(v, mij + 1, dr)
    return cauta_varf(v, st, mij)


print(cauta_varf(v, 0, len(v) - 1))
