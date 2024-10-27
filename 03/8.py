n = int(input("n = "))

primul_par = None
for i in range(n):
    nr = int(input())
    if primul_par is None and nr % 2 == 0:
        primul_par = nr

if primul_par is None:
    print("IMPOSIBIL")
else:
    print(primul_par)
