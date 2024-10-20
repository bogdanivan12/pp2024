n = int(input("n = "))
p = int(input("p = "))

putere = 0
while n % p == 0:
    putere += 1
    n //= p

print(putere)
