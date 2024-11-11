propozitie = input()
s = input()
t = input()

l = propozitie.split()
primul_cuvant = l[0]
ultimul_cuvant = l[-1]
propozitie = propozitie.replace(f" {s} ", f" {t} ")

if primul_cuvant == s:
    propozitie = t + propozitie[len(s):]
if ultimul_cuvant == s:
    propozitie = propozitie[:-len(s)] + t

print(propozitie)
