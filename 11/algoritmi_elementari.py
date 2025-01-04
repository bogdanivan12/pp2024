def nr_cifre_iterativ(n):
    nr_cif = 1
    while n > 9:
        nr_cif += 1
        n //= 10
    return nr_cif


def nr_cifre_recursiv(n):
    if n <= 9:
        return 1
    return 1 + nr_cifre_recursiv(n // 10)


def nr_cifre_div3_iterativ(n):
    nr_cif_div3 = 0
    while n > 9:
        if n % 10 % 3 == 0:
            nr_cif_div3 += 1
        n //= 10
    return nr_cif_div3 + (1 if n % 3 == 0 else 0)


def nr_cifre_div3_recursiv(n):
    if n <= 9:
        if n % 3 == 0:
            return 1
        return 0
    if n % 10 % 3 == 0:
        return 1 + nr_cifre_div3_recursiv(n // 10)
    return nr_cifre_div3_recursiv(n // 10)
