n = int(input("n = "))

copie_n = n
rasturnat = 0
while copie_n > 0:
    rasturnat = rasturnat * 10 + copie_n % 10
    copie_n = copie_n // 10

if n == rasturnat:
    print(f"{n} este palindrom")
else:
    print(f"{n} nu este palindrom")
