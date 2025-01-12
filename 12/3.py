p = int(input("p = "))
n = int(input("n = "))
sol = []


def verif(nr):
    if nr == 0:
        return False
    cifre = set(str(nr))
    return len(cifre) == len(str(nr))


def backtracking(nr=0):
    global p, n, sol
    if len(sol) == p:
        return
    if len(str(nr)) == n:
        sol.append(nr)
        return
    for cifra in range(1, 10):
        if verif(nr * 10 + cifra):
            backtracking(nr * 10 + cifra)


backtracking()
print(sol)
