s = input("s = ")
t = input("t = ")
k = int(input("k = "))

len_t = len(t)
poz = []

i = 0
while i < len(s) - len_t + 1:
    if s[i:i+len_t] == t:
        poz.append(i)
        i += len_t
    else:
        i += 1

if len(poz) < k:
    print("imposibil")
else:
    for i in range(k):
        print(poz[i], end=" ")
