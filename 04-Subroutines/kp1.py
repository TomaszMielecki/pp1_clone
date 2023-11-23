def f(a,b):
    if a>b:
        x=a-b
        wynik=f"{a}-{b}={x}"
    else:
        x=a+b
        wynik=f"{a}+{b}={x}"

    return wynik

print(f(20,8))
print(f(8,12))
print(f(7,7))


