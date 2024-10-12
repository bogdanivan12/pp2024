a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a != 0:
    print(f"x = {(c - b) / a}")
elif b == c:  # a == 0
    print("x apartine multimii R")
else:  # a == 0 si b != c
    print("Ecuatia nu are solutie")
