def f(amount_to_pay):
    amount_to_pay = int(amount_to_pay)

    zl5 = amount_to_pay//5
    reszta5zl = amount_to_pay%5

    zl2 = reszta5zl//2
    reszta2zl = reszta5zl%2

    zl1 = reszta2zl

    wynik = zl5 + zl2 + zl1

    return wynik

print(f(23))
print(f(8))
print(f(2))
print(f(0))

