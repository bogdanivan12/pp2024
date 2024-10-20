x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

if x >= y and x >= z:
    d = x
elif y >= x and y >= z:
    d = y
else:
    d = z

if x <= y and x <= z:
    d -= x
elif y <= x and y <= z:
    d -= y
else:
    d -= z

print(d)
