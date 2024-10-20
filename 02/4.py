z, l, a = input().split(".")
z = int(z)
l = int(l)
a = int(a)

if l in [1, 3, 5, 7, 8, 10]:
    if z == 31:
        z = 1
        l += 1
    else:
        z += 1
elif l in [4, 6, 9, 11]:
    if z == 30:
        z = 1
        l += 1
    else:
        z += 1
elif l == 12:
    if z == 31:
        a += 1
        z = 1
        l = 1
    else:
        z += 1
elif l == 2:
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        if z == 29:
            z = 1
            l += 1
        else:
            z += 1
    else:
        if z == 28:
            z = 1
            l += 1
        else:
            z += 1

print(f"{z}.{l}.{a}")
