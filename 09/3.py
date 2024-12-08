f = open("rime.in", "r")
cuvinte = f.read().split()
f.close()
p = int(input("p = "))

grupuri_dict = {}
for cuvant in cuvinte:
    ultimele_p = cuvant[-p:]
    if ultimele_p not in grupuri_dict:
        grupuri_dict[ultimele_p] = []
    grupuri_dict[ultimele_p].append(cuvant)

grupuri = list(grupuri_dict.values())
grupuri.sort(key=len, reverse=True)
for grup in grupuri:
    grup.sort(reverse=True)

g = open("rime.txt", "w")
for grup in grupuri:
    g.write(" ".join(grup) + "\n")
g.close()
