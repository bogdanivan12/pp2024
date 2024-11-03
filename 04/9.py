text = input("textul = ")
k = int(input("k = "))

criptat = ""
for caracter in text:
    if caracter.isupper():
        criptat += chr((ord(caracter) - ord("A") + k) % 26 + ord("A"))
    elif caracter.islower():
        criptat += chr((ord(caracter) - ord("a") + k) % 26 + ord("a"))
    else:
        criptat += caracter

print(criptat)


# cerinta 2
text = input("textul = ")
k = int(input("k = "))

decriptat = ""
for caracter in text:
    if caracter.isupper():
        decriptat += chr((ord(caracter) - ord("A") - k) % 26 + ord("A"))
    elif caracter.islower():
        decriptat += chr((ord(caracter) - ord("a") - k) % 26 + ord("a"))
    else:
        decriptat += caracter

print(decriptat)
