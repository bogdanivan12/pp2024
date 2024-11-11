nume, *note = input().rsplit(" ", 5)
note = [int(nota) for nota in note]

suma = 0
for nota in note:
    suma += nota

max_nota = max(note)
medie = suma / 5
print(f"Studentul {nume} are media {medie:.2f} si nota maxima {max_nota}")
