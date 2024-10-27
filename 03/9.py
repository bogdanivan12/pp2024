n = int(input("n = "))

ultimul_prim = None
for i in range(1, n + 1):
    nr = int(input())
    prim = True
    if nr in [0, 1]:
        prim = False
    for j in range(2, nr):
        if nr % j ==0:
            prim = False
    if prim:
        ultimul_prim = nr

if ultimul_prim is not None:
    print(ultimul_prim)
else:
    print("IMPOSIBIL")
