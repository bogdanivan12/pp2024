n = int(input("n = "))

for i in range(2, n + 1):
    p = 0
    while n % i == 0:
        p += 1
        n = n // i
    if p > 0:
        print(f"{i}^{p}")
