def f(n1,n2,n3):
    n1=int(n1)
    n2=int(n2)
    n3=int(n3)

    a=max(n1,n2,n3)
    b=min(n1,n2,n3)

    wynik = a-b

    return wynik

print(f(7,4,9) )
print(f(2,12,8) )
