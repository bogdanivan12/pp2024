a = int(input("a = "))
b = int(input("b = "))

# pe aceeasi linie
print(a + b, a * b)  # separate prin spatiu
print(a + b, a * b, sep=",")  # separate prin virgula

# pe linii diferite
print(a + b)
print(a * b)
# sau
print(a + b, a * b, sep="\n")

# mesaj de forma "suma numerelor ... si ... este ..., iar produsul este ..."
print("suma numerelor ", a, " si ", b, " este ", a + b, ", iar produsul este: ", a * b, sep="")
print(f"suma numerelor {a} si {b} este {a + b}, iar produsul este: {a * b}")
