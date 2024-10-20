a = float(input("a = "))
b = float(input("b = "))
x = float(input("x = "))

if a <= x <= b:
    print(f"{x} apartine intervalului [{a}, {b}]")
else:
    print(f"{x} NU apartine intervalului [{a}, {b}]")
