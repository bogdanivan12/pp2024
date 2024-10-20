n = int(input("n = "))

nr_cifre_pare = 0
nr_cifre_impare = 0

if n == 0:
    nr_cifre_pare = 1

while n != 0:
    if n % 2 == 0:
        nr_cifre_pare += 1
    else:
        nr_cifre_impare += 1
    n = n // 10

print(f"Numarul {n} are {nr_cifre_pare} cifre pare si {nr_cifre_impare} cifre impare")
