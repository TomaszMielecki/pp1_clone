def f(n1,n2,operator):
    n1 = int(n1)
    n2 = int(n2)
    operator = str(operator)

    suma = 0

    if operator == "+":
        suma = n1+n2
    elif operator == "-":
        suma = n1-n2
    elif operator == "*":
        suma = n1*n2
    elif operator == "%":
        suma = n1%n2
    elif operator == "**":
        suma = n1**n2
    return suma

print(f(2,3,"+"))
print(f(2,3,"%"))
print(f(2,3,"**"))
print(f(2,3,"*"))
print(f(2,3,"-"))