i1, i2 = input("Introduceti numerele intregi: ").split()
i1 = int(i1)
i2 = int(i2)
f1, f2 = input("Introduceti numerele reale: ").split()
f1 = float(f1)
f2 = float(f2)
c1, c2 = input("Introduceti caracterele: ").split()

# toate pe un singur rand
print(i1, i2, f1, f2, c1, c2)

# fiecare pe cate un rand
print(i1, i2, f1, f2, c1, c2, sep="\n")

# cate doua pe rand
print(f"{i1} {i2}\n{f1} {f2}\n{c1} {c2}")
