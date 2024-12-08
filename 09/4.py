n = int(input("n = "))
persoane_per_luna = {}
for i in range(n):
    persoana = input().split()
    nume = persoana[:-1]
    data_nastere = persoana[-1]
    zi, luna, an = [int(x) for x in data_nastere.split(".")]
    if luna not in persoane_per_luna:
        persoane_per_luna[luna] = []
    persoane_per_luna[luna].append(
        {
            "nume": " ".join(nume),
            "an": an
        }
    )

NUME_LUNI = {
    1: "Ianuarie",
    2: "Februarie",
    3: "Martie",
    4: "Aprilie",
    5: "Mai",
    6: "Iunie",
    7: "Iulie",
    8: "August",
    9: "Septembrie",
    10: "Octombrie",
    11: "Noiembrie",
    12: "Decembrie"
}
for luna in persoane_per_luna:
    print(NUME_LUNI[luna] + ":")
    for persoana in persoane_per_luna[luna]:
        print(f'{persoana["nume"]}, {persoana["an"]}')
