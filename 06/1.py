propozitie = input()
cuvinte = propozitie.split()
ls = [cuvant for cuvant in cuvinte if cuvant[0] in 'aeiouAEIOU']
print(ls)

# SAU
print([cuvant for cuvant in input().split() if cuvant[0] in "aeiouAEIOU"])
