file = open("multimi.in", "r")
multime_de_multimi = {frozenset(int(x) for x in linie.split())
                      for linie in file.readlines()}
file.close()
print(len(multime_de_multimi))
