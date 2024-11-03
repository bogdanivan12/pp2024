s = input()
n = len(s)
for divizor in range(n // 2, 0, -1):
    t = s[:divizor]
    if n % divizor == 0 and t * (n // divizor) == s:
        print(t)
        break
