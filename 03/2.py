a = int(input("a = "))
b = int(input("b = "))

# prin scaderi repetate
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(a)

# prin impartiri repetate
while b != 0:
    rest = a % b
    a = b
    b = rest
print(a)
