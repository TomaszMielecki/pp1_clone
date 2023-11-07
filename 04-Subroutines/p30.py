def f(number,even):
    number = str(number)
    even = bool(even)

    suma = 0

    if even == True:
        for cyfra in number:
            if int(cyfra)%2 == 0:
                suma = suma+int(cyfra)
            else:
                continue
        return suma
    elif even == False:
        for cyfra in number:
            if int(cyfra)%2 == 1:
                suma = suma+int(cyfra)
            else:
                continue
    return suma

print(f(3124,True))
print(f(3124,False))
print(f(20576,False))
print(f(20576,True))
print(f(13115,True))