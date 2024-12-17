prop = input().split()

maxim = max([len(cuvant) for cuvant in prop])
print(maxim)

for cuvant in prop:
    if len(cuvant) == maxim:
        print(cuvant, end=" ")
