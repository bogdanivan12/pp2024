def citire_produse():
    f = open("produse.in", "r")
    produse = f.readlines()
    f.close()
    categorii_dict = {}
    for linie in produse:
        nume, categorie, cantitate, pret = linie.split(" % ")
        cantitate = int(cantitate)
        pret = float(pret)
        if categorie not in categorii_dict:
            categorii_dict[categorie] = 0
        categorii_dict[categorie] += cantitate * pret
    return categorii_dict


categorii_dict = citire_produse()
print(categorii_dict)


def total_vanzari(categorii_dict):
    s = 0
    for cheie in categorii_dict:
        s += categorii_dict[cheie]
    return s
    # SAU
    # return sum(categorii_dict.values())


print(total_vanzari(categorii_dict))

sume_categorii = []
for categorie in categorii_dict:
    sume_categorii.append((categorie, categorii_dict[categorie]))
sume_categorii.sort(key=lambda x: x[1], reverse=True)

g = open("vanzari.out", "w")
for tuplu in sume_categorii:
    g.write(f"{tuplu[0]} {tuplu[1]}\n")
g.write(f"Total: {total_vanzari(categorii_dict)}")
g.close()
