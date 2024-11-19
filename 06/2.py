lista = [int(x) for x in input().split()]
rezultat = [lista[i] for i in range(len(lista)) if i % 2 == lista[i] % 2]
print(rezultat)
