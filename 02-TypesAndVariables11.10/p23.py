a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

p = 1/2*(a+ b + c)
area = sqrt(p*(p-a)*(p-b)*(p-c))
circumference = a+b+c

print(f"Triangle area: {area}")
print(f"Triangle circumference: {circumference}")