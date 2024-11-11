cuvinte = input().split()

cuvinte_sortate = []

for cuvant in cuvinte:
    cuvinte_sortate.append("".join(sorted(cuvant)))

print(" ".join(cuvinte_sortate))
