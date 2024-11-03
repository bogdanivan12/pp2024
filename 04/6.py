propozitie = input()
lmax = 0
propozitie = propozitie.split(", ")
for cuvant in propozitie:
    if len(cuvant) > lmax:
        lmax = len(cuvant)
print(lmax)
