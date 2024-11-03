s = input()
criptat = ""
for litera in s:
    criptat += chr(ord("Z") - ord(litera) + ord("A"))
print(criptat)
