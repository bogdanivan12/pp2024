file = open("cd.in" , "r")
n = int(file.readline())
a = int(file.readline())
b = int(file.readline())
ore_totale = {x for x in range(a, b)}
ore_ocupate = {int(file.readline()) for g in range(n)}
ore_libere = ore_totale - ore_ocupate
print(ore_libere)
