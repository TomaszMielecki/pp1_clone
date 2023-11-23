def f(n):
    n = int(n)
    wynik = ""

    for i in range (1,n+1):
        wynik = wynik+str(i)
    return wynik

print(f(11))
print(f(4))