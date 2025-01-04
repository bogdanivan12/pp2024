import algoritmi_elementari


def filtrare_nr_cifre(*lista, c):
    nr_numere_bune = 0
    for nr in lista:
        if algoritmi_elementari.nr_cifre_recursiv(nr) >= c:
            nr_numere_bune += 1
    return nr_numere_bune


print(filtrare_nr_cifre(15, 19, 178, 2856, c=4))
