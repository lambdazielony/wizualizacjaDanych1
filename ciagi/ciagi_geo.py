def g_nty_wyraz(a1=0, q=0, n=0):
    return (a1 * (q ** (n - 1)))


def g_suma_pocz(a1=0, q=0, n=0):
    return a1 * ((1 - (q ** n)) / (1 - q))
