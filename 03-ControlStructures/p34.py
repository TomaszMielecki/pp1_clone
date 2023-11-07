def f(pln):

    zl5 = pln//5
    reszta5zl = pln%5

    zl2 = reszta5zl//2
    reszta2zl = reszta5zl%2

    zl1 = reszta2zl

    return f"The amount of {pln} PLN in coins: \n 5zł - {zl5} \n 2zł - {zl2} \n 1zł - {zl1}"

print(f(18))