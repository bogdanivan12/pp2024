n = int(input("n = "))

raspuns = 1
for i in range(2, n + 1):
    p = 0
    while n % i == 0:
        p += 1
        n = n // i
    if p > 0:
        raspuns *= i

print(raspuns)
