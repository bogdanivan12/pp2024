bancnote = [25, 10, 5, 1]
frecv = {bancnota: 0 for bancnota in bancnote}

s = int(input("s = "))

for bancnota in bancnote:
    frecv[bancnota] = s // bancnota
    s %= bancnota
    if s == 0:
        break

for bancnota in bancnote:
    if frecv[bancnota] != 0:
        print(f"{frecv[bancnota]} bancnote de {bancnota}")
