n = int(input("n = "))

ultima_cifra = n % 10
toate_egale = True
while n != 0:
    if n % 10 != ultima_cifra:
        toate_egale = False
        break
    n = n // 10

print(toate_egale)
