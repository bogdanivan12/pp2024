x, op, y = input().split()
x = float(x)
y = float(y)

if op == "+":
    print(f"{x} {op} {y} = {x + y:.2f}")
elif op == "-":
    print(f"{x} {op} {y} = {x - y:.2f}")
elif op == "*":
    print(f"{x} {op} {y} = {x * y:.2f}")
elif op == "/":
    print(f"{x} {op} {y} = {x / y:.2f}")
else:
    print(f"Operatorul {op} este invalid")
