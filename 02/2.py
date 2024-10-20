a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Ecuatia nu are solutii reale")
elif delta == 0:
    x = -b / (2 * a)
    print(x)
else:
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    print (x1, x2)
