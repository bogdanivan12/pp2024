p = int(input("p = "))
n = int(input("n = "))
sol = []


def verif(nr):
    if nr == 0:
        return False
    while nr > 9:
        if nr % 100 % 11 == 0:
            return False
        nr //= 10
    return True


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
