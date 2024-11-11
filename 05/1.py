s, c = input().split()
if s.count(c) < 3:
    print("Imposibil")
else:
    poz1 = s.rfind(c)
    poz2 = s[:poz1].rfind(c)
    poz3 = s[:poz2].rfind(c)
    print(poz3, poz2, poz1)

    # SAU

    poz = [i for i in range(len(s)) if s[i] == c][-3:]
    print(*poz)
