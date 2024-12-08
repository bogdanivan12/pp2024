l = [int(x) for x in input().split()]
frecventa = [0] * 101
nr_perechi = 0
for nr in l:
    frecventa[nr] += 1
    if frecventa[nr] % 2 == 0:
        nr_perechi += 1
print(nr_perechi)

# SAU

l = [int(x) for x in input().split()]
frecventa = [0] * 101
nr_perechi = 0
for nr in l:
    frecventa[nr] += 1
for nr in range(1, 101):
    nr_perechi += frecventa[nr] // 2
print(nr_perechi)
