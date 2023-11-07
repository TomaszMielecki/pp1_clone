def f(n):
    n = int(n)

    wynik = ""

    if n<0:
        wynik = wynik+"podaj liczbe"
    elif n == 1:
        wynik = wynik+"*"
    elif n>1:
        for i in range (0,n-1):
            wynik = wynik+"*/"
        wynik=wynik+"*"
    return wynik

print(f(4))
print(f(1))
print(f(7))
    
    