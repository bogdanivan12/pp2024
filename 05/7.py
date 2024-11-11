text = input()

for semn in ",!?;:":
    text = text.replace(semn, " ")

propozitii = text.split(".")
max_a = 0
min_cuv = len(propozitii[0].split())
for propozitie in propozitii:
    nr_a_uri = propozitie.count("a")
    if nr_a_uri > max_a:
        max_a = nr_a_uri

    nr_cuvinte = len(propozitie.split())
    if nr_cuvinte < min_cuv:
        min_cuv = nr_cuvinte

print("Propozitiile cu cele mai multe a-uri:")
for propozitie in propozitii:
    if propozitie.count("a") == max_a:
        print(propozitie.strip())

print("Propozitiile cu cele mai putine cuvinte:")
for propozitie in propozitii:
    if len(propozitie.split()) == min_cuv:
        print(propozitie.strip())

print("Cuvintele doar din litere mari, cu lungime minim 3:")
for cuvant in text.split():
    if len(cuvant) >= 3 and cuvant.isupper():
        print(cuvant)
