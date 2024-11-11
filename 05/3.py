l = [float(x) for x in input().split()]

s = 0
for x in l:
    s += x

print("(",end="")
print(" + ".join([str(x) for x in l]), end="")
print(f") / {len(l)} = {s / len(l):.1f}")
