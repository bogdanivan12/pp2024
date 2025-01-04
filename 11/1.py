def nr_vocale(cuvant):
    nr_voc = 0
    for litera in cuvant:
        if litera in "aeiouAEIOU":
            nr_voc += 1
    return nr_voc


cuvinte = input().split()
cuvinte.sort(key=lambda cuvant: (nr_vocale(cuvant), cuvant))
print(cuvinte)
