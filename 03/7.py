n = int(input("n = "))

# primii n termeni
a = 0
b = 1
for i in range(n):
    print(b, end = " ")
    c = a + b
    a = b
    b = c

print()

# termenii mai mici decat n
a = 0
b = 1
while b < n:
    print(b, end = " ")
    c = a + b
    a = b
    b = c
