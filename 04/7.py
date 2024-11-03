w = input("w = ")
p = int(input("p = "))
n = int(input("n = "))
cuvinte_bune = []
for i in range(n):
    cuvant = input()
    if len(cuvant) >= p + 2 and cuvant[-p:] == w[-p:]:
        cuvinte_bune.append(cuvant)

# print(*cuvinte_bune)
for cuvant in cuvinte_bune:
    print(cuvant, end=" ")

# cerinta 2
w = input("w = ")
p = int(input("p = "))
propozitie = input("propozitie = ")
cuvinte_bune = []
for cuvant in propozitie.split():
    if len(cuvant) >= p + 2 and cuvant[-p:] == w[-p:]:
        cuvinte_bune.append(cuvant)

# print(*cuvinte_bune)
for cuvant in cuvinte_bune:
    print(cuvant, end=" ")
