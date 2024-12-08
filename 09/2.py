f = open("elevi.in", "r")
elevi_dict = {}
elevi = f.readlines()
f.close()
for linie in elevi:
    date = linie.split()
    elevi_dict[int(date[0])] = {"nume": date[1] + " " + date[2],
                                "note": [int(x) for x in date[3:]]}
cnp = int(input("cnp = "))
print(elevi_dict.get(cnp, "Nu exista acest cnp"))


def incrementare_prima_nota(cnp, dictionar_elevi):
    if cnp not in dictionar_elevi:
        return None
    dictionar_elevi[cnp]["note"][0] += 1
    return dictionar_elevi[cnp]["note"][0]


cnp = int(input("cnp = "))
print(incrementare_prima_nota(cnp, elevi_dict))
print(elevi_dict)


def adauga_note(cnp, lista_note, dictionar_elevi):
    if cnp not in dictionar_elevi:
        return None
    dictionar_elevi[cnp]["note"].extend(lista_note)
    return dictionar_elevi[cnp]["note"]


cnp = int(input("cnp = "))
lista_note = [int(x) for x in input().split()]
print(adauga_note(cnp, lista_note, elevi_dict))
print(elevi_dict)
