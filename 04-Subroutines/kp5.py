def f(a,b):
    a=int(a)
    b=int(b)

    wynik=""

    if b%2==0:
        last = b
    elif b%2!=0:
        last=b-1


    if a<b:
        for i in range (a,b+1):
            if i%2==0 and i!=last:
                wynik=wynik+str(i)+","
            elif i%2==0 and i==last:
                wynik=wynik+str(i)
            else:
                continue
        return wynik
    else:
        return False
    
print(f(2,3))
print(f(3,11))
print(f(4,6))

