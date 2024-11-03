cuvant = input()

for i in range(len(cuvant) - 1, 0, -1):
    prefix = cuvant[:i]
    oglindit = prefix[::-1]
    if prefix == oglindit:
        print(prefix)
        break

# SAU

prefix = cuvant
while prefix != "":
    oglindit = prefix[::-1]
    if prefix == oglindit:
        print(prefix)
        break
    prefix = prefix[:-1]  # eliminam cate o litera de la sfarsitul cuvantului
