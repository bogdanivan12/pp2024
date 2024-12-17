f = open("cuvinte.in", "r")
cuvinte = f.read().split()
f.close()
l = [x for x in cuvinte if x[-1] in "aeiouAEIOU"]
for x in l:
    print(x, end=" ")
