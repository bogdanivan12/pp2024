file = open("multimi.in", "r")
l = [{int(x) for x in linie.split()} for linie in file.readlines()]
file.close()

minim = len(l[0])
for multime in l:
    if len(multime) < minim:
        minim = len(multime)
print(minim)

reuniune = set()
for multime in l:
    if len(multime) == minim:
        print(multime)
        reuniune = reuniune.union(multime)
print(reuniune)
