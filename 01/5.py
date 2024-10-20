a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if 0 <= a <= 23 and 0 <= b <= 59 and 0 <= c <= 59:
    if a < 10:
        a = f"0{a}"
    if b < 10:
        b = f"0{b}"
    if c < 10:
        c = f"0{c}"
    print(f"{a}:{b}:{c}")
else:
    print("Ora introdusa este invalida")
