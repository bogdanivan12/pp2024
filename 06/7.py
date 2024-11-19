ls = [int(x) for x in input().split()]
lmax = 1
l = 1
for i in range(1, len(ls)):
    if ls[i - 1] < ls[i]:
        l += 1
    else:
        if l > lmax:
            lmax = l
        l = 1
if l > lmax:
    lmax = l
print(lmax)
