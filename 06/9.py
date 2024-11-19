l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]

l1.sort()
l2.sort()

proportionale = True
for i in range(len(l1)):
    if l1[0] * l2[i] != l1[i] * l2[0]:  # produsul pe diagonala al raportului
        proportionale = False
        break

print("DA" if proportionale else "NU")
