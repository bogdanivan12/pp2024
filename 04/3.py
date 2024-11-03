propozitie = input("Propozitia este: ")
cuvinte = propozitie.split()

nr_cuvinte_bune = 0
for cuvant in cuvinte:
    if len(cuvant) > 2 and cuvant[-1] in "aeiouAEIOU":
        nr_cuvinte_bune += 1

print(nr_cuvinte_bune)
